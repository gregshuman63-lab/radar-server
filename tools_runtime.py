import importlib

# Map runner -> module
def _module_for_runner(runner: str) -> str:
    return {"python": "tools_fs"}[runner]

def execute_plan(plan: dict):
    results = []
    for step in plan.get("steps", []):
        tool = step["tool"]
        args = step.get("args", {}) or {}
        label = step.get("label")

        # Lookup tool definition from tools.yaml-like assumptions:
        # We hardcode the simple mapping for Day-0 Mini:
        if tool == "fs.search":
            runner = "python"
            func_name = "fs_search"
        else:
            raise RuntimeError(f"Unknown tool: {tool}")

        mod = importlib.import_module(_module_for_runner(runner))
        func = getattr(mod, func_name)
        out = func(**args)

        results.append({
            "step_id": step["id"],
            "tool": tool,
            "label": label,
            "output": out
        })
    return results
