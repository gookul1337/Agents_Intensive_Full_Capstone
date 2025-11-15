from src.tools import ToolRegistry

class PlannerAgent:
    def __init__(self, name='Planner'):
        self.name = name

    def plan(self, query:str)->Dict[str,Any]:
        # Very simple decomposition: split by sentences or create 2 subtasks
        subtasks = [query + ' - background', query + ' - specifics']
        return {'agent': self.name, 'action': 'plan', 'subtasks': subtasks}
