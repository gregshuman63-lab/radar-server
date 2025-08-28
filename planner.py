import yaml
from pathlib import Path

with open(Path(__file__).parent / "tools.yaml", "r", encoding="utf-8") as f:
    TOOL_REG = yaml.safe_load(f)

def _has_tool(name: str) -> bool:
    return any(t["name"] == name for t in TOOL_REG["tools"])

def plan(refine_spec: dict) -> dict:
    goal = (refine_spec.get("goal") or "").lower()
    steps = []

    # Bare minimum: if the user mentions pdf, search Downloads only
    if "pdf" in goal and _has_tool("fs.search"):
        steps.append({
            "id": "s1",
            "tool": "fs.search",
            "args": {"pattern": "*.pdf", "start_dir": "~/Downloads"},
            "label": "Downloads"
        })

    # If no step matched, default to a small, harmless list of txt files in Downloads
    if not steps and _has_tool("fs.search"):
        steps.append({
            "id": "s1",
            "tool": "fs.search",
            "args": {"pattern": "*.txt", "start_dir": "~/Downloads"},
            "label": "Downloads"
        })

    return {"steps": steps, "approval_checkpoints": []}
