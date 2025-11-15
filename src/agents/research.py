import os
import json
import requests

from tools import ToolRegistry


class ResearchAgent:
    """
    Research agent that uses Google API Studio Web Search.
    Falls back to stub mode if API key is missing.
    """

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
        self.use_stub = self.api_key is None or self.api_key.strip() == ""

        if self.use_stub:
            print("⚠️ GOOGLE_SEARCH_API_KEY not found — using stub search mode.")
        else:
            print("✅ Google Web Search API enabled.")

    def google_search(self, query):
        """
        Real web search via Google API Studio Web Search.
        """
        url = "https://search.googleapis.com/v1/web:search"
        params = {
            "q": query,
            "key": self.api_key,
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {
                "query": query,
                "summary": "Search failed",
                "hits": []
            }

        data = response.json()

        hits = []
        for item in data.get("results", []):
            hits.append({
                "title": item.get("title", ""),
                "snippet": item.get("snippet", "")
            })

        # Summarize based on snippets
        summary_text = "\n".join([h["snippet"] for h in hits]) or "No results found"

        return {
            "query": query,
            "summary": summary_text,
            "hits": hits
        }

    def run(self, query: str):
        """
        Main method: performs search and summarization.
        """
        if self.use_stub:
            # Use fallback stub implementations
            return {
                "query": query,
                "summary": summarize_stub(query),
                "hits": web_search_stub(query)
            }

        # Real search
        result = self.google_search(query)

        # Extra summarization (optional)
        result["summary"] = summarize_stub(result["summary"])

        return result
