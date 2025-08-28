def refine(utterance: str) -> dict:
    u = (utterance or "").strip()
    return {
        "context": "local",
        "goal": u,
        "subgoals": [],
        "inputs": [],
        "verification": "Return structured outputs per step",
        "risk_level": "low",
    }
