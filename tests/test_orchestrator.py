from orchestrator import Orchestrator
def test_orchestrator_runs():
    o = Orchestrator(n_agents=3)
    t = o.run(query='test query', steps=2)
    assert isinstance(t, list)
    assert any(s.get('step')=='final' or 'final' in s.get('step','') for s in t)
