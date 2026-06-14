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
        
        # -> Click the 'Checkout Service' entry in the Apps list to select the mock application.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'API Gateway' node on the canvas to open the Node Inspector and display its details.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Runtime' tab in the Node Inspector to view runtime information for the selected node.
        # Runtime button
        elem = page.get_by_role('tab', name='Runtime', exact=True)
        await elem.click(timeout=10000)
        
        # -> click
        # Config button
        elem = page.get_by_role('tab', name='Config', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Runtime' tab in the Node Inspector to display runtime information for the selected node and verify the runtime panel appears.
        # Runtime button
        elem = page.get_by_role('tab', name='Runtime', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Config' tab in the Node Inspector to switch back to the configuration view and verify that the configuration fields (Node name, Description, Load) are displayed.
        # Config button
        elem = page.get_by_role('tab', name='Config', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify configuration fields are displayed
        # Assert: The Node name input contains the node name 'API Gateway'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[1]/input").nth(0)).to_have_value("API Gateway", timeout=15000), "The Node name input contains the node name 'API Gateway'."
        # Assert: The Description field shows 'Routes incoming checkout requests'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[2]/textarea").nth(0)).to_have_text("Routes incoming checkout requests", timeout=15000), "The Description field shows 'Routes incoming checkout requests'."
        # Assert: The Load numeric input displays the value 42.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[3]/div/input").nth(0)).to_have_value("42", timeout=15000), "The Load numeric input displays the value 42."
        current_url = await page.evaluate("() => window.location.href")
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    