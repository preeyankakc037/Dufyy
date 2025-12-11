# views.py
import os
import logging
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.decorators.cache import cache_page  # Optional: cache trending
from urllib.parse import quote  # For URL encoding

from .utils.search_engine import search_songs
from .utils.spotify_api import get_spotify_trending

logger = logging.getLogger(__name__)

# =========================================
# LOAD DATASET
# =========================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "recommendations", "data", "test.csv")
dataset = pd.DataFrame()

def load_dataset():
    global dataset
    if not os.path.exists(DATASET_PATH):
        logger.error(f"CSV NOT FOUND: {DATASET_PATH}")
        return
    try:
        dataset = pd.read_csv(DATASET_PATH)
        dataset.fillna("", inplace=True)
        logger.info(f"LOADED {len(dataset)} SONGS")
    except Exception as e:
        logger.error(f"CSV ERROR: {e}")

load_dataset()

# =========================================
# API & VIEWS
# =========================================
@csrf_exempt
def get_recommendations(request):
    query = request.GET.get("query", "").strip().lower()
    
    if dataset.empty:
        return JsonResponse({"recommendations": []}, safe=False)
    
    if not query or query in ["popular", "trending", "home", ""]:
        songs = dataset.sample(n=min(30, len(dataset))).to_dict("records")
        return JsonResponse({"recommendations": songs}, safe=False)
    
    if "genre" in dataset.columns and query in dataset["genre"].str.lower().unique():
        genre_songs = dataset[dataset["genre"].str.lower() == query]
        songs = genre_songs.sample(n=min(30, len(genre_songs))).to_dict("records")
        return JsonResponse({"recommendations": songs}, safe=False)
    
    try:
        results = search_songs(query, top_k=30)
        return JsonResponse({"recommendations": results}, safe=False)
    except:
        fallback = dataset.sample(n=min(20, len(dataset))).to_dict("records")
        return JsonResponse({"recommendations": fallback}, safe=False)


def discover_view(request):
    songs = dataset.sample(n=min(30, len(dataset))).to_dict("records") if not dataset.empty else []
    return render(request, 'discover.html', {"songs": songs})

def genre_view(request):
    genres = dataset["genre"].dropna().str.title().unique().tolist() if "genre" in dataset.columns and not dataset.empty else []
    return render(request, 'genre.html', {"genres": sorted(genres)})

def community(request):
    songs = dataset.sample(n=min(50, len(dataset))).to_dict("records") if not dataset.empty else []
    return render(request, 'community.html', {"songs": songs})

def favourites_view(request):
    return render(request, 'favourites.html')

def playlist_view(request):
    return render(request, 'playlist.html')

def signup_view(request):
    return render(request, 'signup.html')

def health_check(request):
    return JsonResponse({
        "status": "OK",
        "total_songs": len(dataset),
        "csv_loaded": not dataset.empty
    })


# Optional: Cache trending for 30 minutes (recommended for production)
@cache_page(60 * 30)
def trending_view(request):
    print("Trending view accessed")
    tracks = get_spotify_trending()

    # Fallback to local dataset if Spotify fails
    if not tracks and not dataset.empty:
        print("Spotify failed → using local trending fallback")
        local_tracks = dataset.sample(n=30).to_dict("records")
        tracks = []
        for t in local_tracks:
            # Map keys to match template: "artist" (singular), add mock spotify_url
            artist_name = t.get("artists", t.get("artist", "Unknown Artist"))  # Handle both singular/plural
            track_name = t.get("name", "Unknown Track")
            # Mock Spotify search URL (opens Spotify search for the song)
            mock_url = f"https://open.spotify.com/search/{quote(track_name)}%20{quote(artist_name)}"
            tracks.append({
                "name": track_name,
                "artists": artist_name,  # Use as "artists" for Spotify, but template uses "artist"
                "image": t.get("image", "https://via.placeholder.com/300?text=Music"),
                "url": mock_url  # Use "url" to match Spotify format
            })
    else:
        # Spotify success: Map to template keys (template uses "artist" singular)
        songs = []
        for t in tracks:
            songs.append({
                "name": t.get("name", "Unknown"),
                "artist": t.get("artists", "Unknown Artist"),  # Map "artists" → "artist"
                "image": t.get("image", "https://via.placeholder.com/300?text=No+Image"),
                "spotify_url": t.get("url", "#")
            })
        return render(request, "trending.html", {"songs": songs})

    # Fallback case: Map to template keys
    songs = []
    for t in tracks:
        songs.append({
            "name": t.get("name", "Unknown"),
            "artist": t.get("artists", "Unknown Artist"),  # Ensure singular "artist"
            "image": t.get("image", "https://via.placeholder.com/300?text=No+Image"),
            "spotify_url": t.get("url", "#")  # Now has mock URL
        })

    return render(request, "trending.html", {"songs": songs})