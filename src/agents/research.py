import os
import requests

API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")

class ResearchAgent:
    """
    Research agent using Google's NEW Web Search API (API Studio).
    """

    def run(self, query):
        if not API_KEY:
            return {
                "query": query,
                "summary": "ERROR: Missing GOOGLE_SEARCH_API_KEY.",
                "hits": []
            }

        url = "https://websearch.googleapis.com/v1/web:search"

        params = {
            "q": query,
            "key": API_KEY,
            "num": 5
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            items = data.get("results", [])
            top_items = items[:3]

            summary = (
                top_items[0]["snippet"]
                if top_items else "No real search results found."
            )

            return {
                "query": query,
                "summary": summary,
                "hits": top_items
            }

        except Exception as error:
            return {
                "query": query,
                "summary": f"Search error: {error}",
                "hits": []
            }
