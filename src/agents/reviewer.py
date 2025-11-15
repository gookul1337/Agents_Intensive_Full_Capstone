from typing import Dict, Any

class ReviewerAgent:
    def __init__(self, name="Reviewer"):
        self.name = name

    def review(self, draft: Dict[str, Any]) -> Dict[str, Any]:
        reviewed = draft["draft"] + "\n\nReview: Looks good!"
        return {
            "agent": self.name,
            "action": "review",
            "final_output": reviewed
        }
