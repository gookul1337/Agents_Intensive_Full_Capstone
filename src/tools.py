class ToolRegistry:
    def web_search_stub(self, query):
        return f"Web search results for: {query}"

    def summarize_stub(self, text):
        return f"Summary: {text[:80]}..."
