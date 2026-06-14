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
        
        # -> Click the 'Payment Service' node on the canvas to open the node inspector and display its configuration.
        # Payment Service Processes card and wallet payments
        elem = page.get_by_role('group', name='Payment Service Processes card and wallet payments', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Runtime' tab in the Node Inspector (the tab labeled 'Runtime') to open the Runtime view for the selected service node.
        # Runtime button
        elem = page.get_by_role('tab', name='Runtime', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Config' tab in the Node Inspector to switch back to the Config view and confirm the inspector shows the selected node's details (name/description/ID).
        # Config button
        elem = page.get_by_role('tab', name='Config', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the node inspector is displayed
        await page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The Node Inspector tab list showing 'Config' and 'Runtime' is visible, confirming the inspector is displayed.
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[1]").nth(0)).to_be_visible(timeout=15000), "The Node Inspector tab list showing 'Config' and 'Runtime' is visible, confirming the inspector is displayed."
        
        # --> Verify the inspector shows the selected node details
        # Assert: The inspector's Node name field shows "Payment Service".
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[1]/input").nth(0)).to_have_value("Payment Service", timeout=15000), "The inspector's Node name field shows \"Payment Service\"."
        # Assert: The inspector's Description field shows the node description.
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[2]/textarea").nth(0)).to_have_value("Processes card and wallet payments", timeout=15000), "The inspector's Description field shows the node description."
        # Assert: The inspector's Load field shows the value 78.
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[3]/div/input").nth(0)).to_have_value("78", timeout=15000), "The inspector's Load field shows the value 78."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    