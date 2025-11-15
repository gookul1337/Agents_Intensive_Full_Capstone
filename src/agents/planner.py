from typing import Dict, Any
from tools import ToolRegistry

class PlannerAgent:
    def __init__(self, name='Planner'):
        self.name = name

    def plan(self, query: str) -> Dict[str, Any]:
        # simple decomposition
        subtasks = [
            query + " - background",
            query + " - specifics"
        ]

        return {
            "agent": self.name,
            "action": "plan",
            "subtasks": subtasks
        }
