import os
import glob
from pathlib import Path

def _expand(p: str) -> str:
    return str(Path(os.path.expanduser(p)).resolve())

def fs_search(pattern: str, start_dir: str):
    root = _expand(start_dir)
    # Use glob recursively; limit top results for speed/readability
    matches = [str(p) for p in Path(root).rglob(pattern)]
    top = matches[:10]
    return {"count": len(matches), "top10": top}
