from typing import Dict, Any, List
from tools import web_search_stub, summarize_stub, ToolRegistry

class ResearchAgent:
    def __init__(self, name='Research', tool_registry:ToolRegistry=None):
        self.name = name
        self.tools = tool_registry or ToolRegistry()
        # register stubs
        self.tools.register('search', web_search_stub)
        self.tools.register('summarize', summarize_stub)

    def research(self, query:str)->Dict[str,Any]:
        hits = self.tools.call('search', query)
        snippets = ' '.join([h['snippet'] for h in hits])
        summary = self.tools.call('summarize', snippets)
        return {'agent': self.name, 'query': query, 'hits': hits, 'summary': summary}
