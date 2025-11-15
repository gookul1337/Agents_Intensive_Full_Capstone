from typing import Dict, Any
from tools import ToolRegistry

class ResearchAgent:
    def __init__(self, name="Researcher"):
        self.name = name
        self.tools = ToolRegistry()

    def research(self, query: str) -> Dict[str, Any]:
        search_result = self.tools.web_search_stub(query)
        summary = self.tools.summarize_stub(search_result)

        return {
            "agent": self.name,
            "action": "research",
            "query": query,
            "result": summary
        }
