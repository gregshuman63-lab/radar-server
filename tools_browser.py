import sys, asyncio, time

# ---- Windows asyncio fix (prevents NotImplementedError) ----
if sys.platform.startswith("win"):
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    except Exception:
        pass
# -----------------------------------------------------------

from playwright.sync_api import sync_playwright

def browser_inspect(url: str):
    with sync_playwright() as p:
        # Open a visible Chromium window
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context()
        page = ctx.new_page()

        # Navigate and wait for the DOM to be ready
        page.goto(url, wait_until="domcontentloaded")

        # Collect simple page metadata
        result = {
            "url": page.url,
            "title": page.title(),
            "forms": page.locator("form").count(),
            "buttons": page.locator("button, input[type=submit]").count(),
        }

        # Keep the window open briefly so you can see it
        time.sleep(3)

        # Clean up
        ctx.close()
        browser.close()

        return result

