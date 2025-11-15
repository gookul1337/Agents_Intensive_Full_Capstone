from typing import List, Dict, Any
from agents.planner import PlannerAgent
from agents.research import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent
from tools import ToolRegistry

class Orchestrator:
    def __init__(self, n_agents:int=3):
        # n_agents currently influences internal config; we create one of each role
        self.planner = PlannerAgent('Planner-1')
        self.research = ResearchAgent('Research-1', tool_registry=ToolRegistry())
        self.writer = WriterAgent('Writer-1')
        self.reviewer = ReviewerAgent('Reviewer-1')

    def run(self, query:str, steps:int=3) -> List[Dict[str,Any]]:
        timeline = []
        # Planner decomposes task
        plan = self.planner.plan(query)
        timeline.append({'step': 'plan', 'output': plan})
        research_outputs = []
        for sub in plan.get('subtasks', []):
            r = self.research.research(sub)
            timeline.append({'step': 'research', 'subtask': sub, 'output': r})
            research_outputs.append(r)
        # Writer composes
        draft = self.writer.write(query, research_outputs)
        timeline.append({'step': 'write', 'output': draft})
        # Reviewer validates
        review = self.reviewer.review(draft)
        timeline.append({'step': 'review', 'output': review})
        # final
        final = {'answer': draft.get('answer'), 'approved': review.get('approved'), 'issues': review.get('issues')}
        timeline.append({'step': 'final', 'output': final})
        return timeline
