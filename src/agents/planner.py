from typing import Dict, Any

class PlannerAgent:
    def __init__(self, name="Planner"):
        self.name = name

    def plan(self, query: str) -> Dict[str, Any]:
        subtasks = [
            query + " — background",
            query + " — details"
        ]
        return {
            "agent": self.name,
            "action": "plan",
            "subtasks": subtasks
        }
