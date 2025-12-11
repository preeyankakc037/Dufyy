# recommendations/views.py (or wherever your view is)
from django.http import JsonResponse
from recommendations.utils.search_engine import search_songs
import logging

logger = logging.getLogger(__name__)

def get_recommendations(request):
    """
    API endpoint: /api/recommend/?query=...
    Returns music recommendations using FAISS + typo fix.
    """
    query = request.GET.get("query", "").strip()

    if not query:
        logger.warning("Empty query received")
        return JsonResponse({"error": "Query parameter is required"}, status=400)

    try:
        results = search_songs(query)  # This uses FAISS + typo fix
        logger.info(f"Search successful: '{query}' → {len(results)} results")
        return JsonResponse({"recommendations": results})

    except Exception as e:
        logger.error(f"Search failed for query='{query}': {str(e)}")
        return JsonResponse({"error": "Internal server error"}, status=500)
    


