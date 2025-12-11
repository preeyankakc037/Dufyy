# utils/spotify_api.py
import requests
from django.conf import settings


def get_spotify_token():
    """Get Spotify access token using Client Credentials flow."""
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET),
        timeout=10
    )

    if response.status_code != 200:
        print("SPOTIFY TOKEN ERROR:", response.status_code, response.text)
        return None

    token = response.json().get("access_token")
    print("Spotify token obtained successfully")
    return token


def get_spotify_trending():
    """Fetch Global Top 50 from a reliable public playlist (updated daily)."""
    token = get_spotify_token()
    if not token:
        return []

    headers = {"Authorization": f"Bearer {token}"}

    # Verified PUBLIC playlist: "Global Top 50 | 2025 Hits" by Topsify
    # 50 items, updated regularly, works with Client Credentials (Nov 2025)
    # Web: https://open.spotify.com/playlist/1KNl4AYfgZtOVm9KHkhPTF
    playlist_id = "1KNl4AYfgZtOVm9KHkhPTF"

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    params = {
        "limit": 50,
        "market": "US"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        print("SPOTIFY PLAYLIST STATUS:", response.status_code)

        if response.status_code != 200:
            print("SPOTIFY PLAYLIST ERROR:", response.json())
            return []

        items = response.json().get("items", [])
        tracks = []

        for item in items:
            track = item.get("track")
            if not track or track.get("is_local"):
                continue

            artists = track.get("artists", [])
            album = track.get("album", {})
            images = album.get("images", [])

            tracks.append({
                "name": track.get("name", "Unknown Track"),
                "artists": ", ".join([a.get("name", "") for a in artists]),
                "image": images[0].get("url") if images else "https://via.placeholder.com/300?text=No+Image",
                "url": track.get("external_urls", {}).get("spotify", "#")
            })

        print(f"Loaded {len(tracks)} trending tracks from Spotify")
        return tracks

    except Exception as e:
        print("EXCEPTION in get_spotify_trending:", str(e))
        return []