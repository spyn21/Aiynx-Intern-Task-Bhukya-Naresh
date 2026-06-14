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
        
        # -> Click the 'Checkout Service' app in the Apps list to ensure the application is selected, then click the 'API Gateway' node on the canvas to open the Node Inspector.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Checkout Service' app in the Apps list to ensure the application is selected, then click the 'API Gateway' node on the canvas to open the Node Inspector.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the node inspector is displayed
        await page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert: Node Inspector panel is visible.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]").nth(0)).to_be_visible(timeout=15000), "Node Inspector panel is visible."
        # Assert: Node Inspector description shows the selected node's description.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[2]/textarea").nth(0)).to_have_text("Routes incoming checkout requests", timeout=15000), "Node Inspector description shows the selected node's description."
        
        # --> Verify selected node details are visible
        # Assert: The Node name field displays 'API Gateway'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[1]/input").nth(0)).to_have_value("API Gateway", timeout=15000), "The Node name field displays 'API Gateway'."
        # Assert: The Description field displays 'Routes incoming checkout requests'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[2]/textarea").nth(0)).to_have_text("Routes incoming checkout requests", timeout=15000), "The Description field displays 'Routes incoming checkout requests'."
        # Assert: The Load field shows the value '42'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[3]/div/input").nth(0)).to_have_value("42", timeout=15000), "The Load field shows the value '42'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    