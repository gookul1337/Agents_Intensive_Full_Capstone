from tools import ToolRegistry


class ReviewerAgent:
    def __init__(self, name='Reviewer'):
        self.name = name

    def review(self, draft:Dict[str,Any])->Dict[str,Any]:
        answer = draft.get('answer','')
        issues = []
        if len(answer) < 50:
            issues.append('Answer too short')
        approved = len(issues) == 0
        return {'agent': self.name, 'approved': approved, 'issues': issues}
