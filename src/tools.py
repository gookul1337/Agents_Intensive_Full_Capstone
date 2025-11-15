# Tool interfaces and stubs. Replace stubs with real implementations.
from typing import Any, Dict, List
import os

class ToolRegistry:
    def __init__(self):
        # provide hooks to real tools (search, summarize, calculator)
        self.tools = {}
    def register(self, name:str, fn):
        self.tools[name]=fn
    def call(self, name:str, *args, **kwargs):
        if name in self.tools:
            return self.tools[name](*args, **kwargs)
        raise RuntimeError(f'Tool {name} not registered')

# Example stubbed tools
def web_search_stub(query:str)->List[Dict[str,str]]:
    # In production, replace with Bing/Google search API
    return [{'title':'Example result','snippet':f'Info about {query} from web (stub)'}]

def summarize_stub(text:str)->str:
    return text[:300] + ('...' if len(text)>300 else '')
