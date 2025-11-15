from src.tools import ToolRegistry


class WriterAgent:
    def __init__(self, name='Writer'):
        self.name = name

    def write(self, prompt:str, research_outputs:List[Dict[str,Any]])->Dict[str,Any]:
        combined = '\n'.join([r['summary'] for r in research_outputs])
        answer = f"Composed answer for: {prompt}\n\nSources summary:\n{combined}\n\nFinal:\nThis is a generated answer (placeholder)."
        return {'agent': self.name, 'answer': answer}
