import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:5173")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Payment Service' node on the canvas to open its details in the Node Inspector.
        # Click the 'Payment Service' node on the canvas to open its details in the Node Inspector.
        elem = page.locator('xpath=/html/body/div/div/div/main/div/div/div/div/div[3]/div[2]/div/div')
        await elem.click(timeout=10000)
        
        # -> Click the 'Runtime' tab in the Node Inspector to open runtime details and reveal runtime metrics for the selected Payment Service node.
        # Runtime button
        elem = page.get_by_role('tab', name='Runtime', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the node status is displayed
        # Assert: The 'Status' label is shown in the Node Inspector.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/span").nth(0)).to_have_text("Status", timeout=15000), "The 'Status' label is shown in the Node Inspector."
        # Assert: The node status 'Degraded' is displayed in the Node Inspector.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[3]").nth(0)).to_contain_text("Degraded", timeout=15000), "The node status 'Degraded' is displayed in the Node Inspector."
        
        # --> Verify runtime metrics are displayed
        # Assert: Runtime panel shows the status 'Degraded'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[3]").nth(0)).to_contain_text("Degraded", timeout=15000), "Runtime panel shows the status 'Degraded'."
        # Assert: Runtime 'Load' numeric input displays 78.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[3]/div[2]/div/input").nth(0)).to_have_value("78", timeout=15000), "Runtime 'Load' numeric input displays 78."
        # Assert: Runtime 'Type' is shown as 'service'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[3]/span[2]").nth(0)).to_have_text("service", timeout=15000), "Runtime 'Type' is shown as 'service'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    