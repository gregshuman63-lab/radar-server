import traceback
from fastapi import FastAPI
from pydantic import BaseModel
from refiner import refine as refiner_refine
from planner import plan as planner_plan
from tools_runtime import execute_plan

app = FastAPI(title="Builder Bot — Day-0 Mini")

class AskIn(BaseModel):
    utterance: str

@app.post("/ask")
def ask(payload: AskIn):
    out = {"ok": True, "error": None, "refine_spec": None, "plan": None, "results": []}
    try:
        refine_spec = refiner_refine(payload.utterance)
        out["refine_spec"] = refine_spec
        plan = planner_plan(refine_spec)
        out["plan"] = plan
        results = execute_plan(plan)
        out["results"] = results
    except Exception as e:
        out["ok"] = False
        out["error"] = f"{type(e).__name__}: {e}"
        out["trace"] = traceback.format_exc()
    return out
