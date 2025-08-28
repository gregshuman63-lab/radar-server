# mediator.py
def rewrite(user_ask: str) -> dict:
    u = user_ask.strip()
    intents = []
    u_low = u.lower()
    if "pdf" in u_low: intents.append("find_pdfs")
    if "learn" in u_low or "http" in u_low: intents.append("inspect_url")
    # You can grow these intents over time.
    prompt = (
        "You are the build strategist. "
        "Summarize the user's goal and produce a short, step-by-step plan using the available tools. "
        "Assume tools: fs.search, browser.inspect. Be specific."
        f"\n\nUser ask: {u}\n"
    )
    return {"original": u, "prompt_for_ai": prompt, "intents": intents or ["general"]}
