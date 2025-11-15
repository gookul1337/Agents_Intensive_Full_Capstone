from typing import List, Dict, Any

from agents.planner import PlannerAgent
from agents.research import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def run(self, query: str) -> List[Dict[str, Any]]:
        timeline = []

        # Step 1: Planning
        plan = self.planner.plan(query)
        timeline.append(plan)

        # Step 2: Research
        research_results = []
        for task in plan["subtasks"]:
            r = self.researcher.research(task)
            research_results.append(r)
        timeline.append({"agent": "ResearchAgent", "action": "research", "output": research_results})

        # Step 3: Writing
        draft = self.writer.write(query, research_results)
        timeline.append(draft)

        # Step 4: Review
        review = self.reviewer.review(draft)
        timeline.append(review)

        return timeline
