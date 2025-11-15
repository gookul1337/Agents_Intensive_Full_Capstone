from typing import Dict, Any, List

class PlannerAgent:
    """
    PlannerAgent breaks a user query into smaller subtasks.
    """

    def plan(self, query: str) -> Dict[str, Any]:
        """
        Returns a dictionary with subtasks for the orchestrator.
        """
        subtasks: List[str] = [
            f"{query} - background",
            f"{query} - specifics"
        ]

        return {
            "step": "plan",
            "agent": "Planner-1",
            "action": "plan",
            "subtasks": subtasks
        }
