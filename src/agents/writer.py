from typing import List, Dict, Any

class WriterAgent:
    def __init__(self, name="Writer"):
        self.name = name

    def write(self, query: str, research_outputs: List[Dict[str, Any]]) -> Dict[str, Any]:
        combined = "\n".join([r["result"] for r in research_outputs])
        draft = f"Draft for '{query}':\n\n{combined}"
        return {
            "agent": self.name,
            "action": "write",
            "draft": draft
        }
