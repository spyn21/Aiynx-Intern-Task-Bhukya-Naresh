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
        
        # -> Select the 'Checkout Service' application from the Apps list, then click the 'Simulate Error' button to enable simulated API errors for the graph.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> Select the 'Checkout Service' application from the Apps list, then click the 'Simulate Error' button to enable simulated API errors for the graph.
        # Simulate Error button
        elem = page.get_by_role('button', name='Simulate Error', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the top-right 'Errors On' button to disable simulated API errors, then retry loading the graph using the central 'Retry' button if it appears.
        # Errors On button
        elem = page.get_by_role('button', name='Errors On', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the top-right 'Errors On' button to disable simulated API errors, then retry loading the graph using the central 'Retry' button if it appears.
        # Retry button
        elem = page.locator("xpath=/html/body/div[1]/div/div/main/div/button").nth(0)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the service dependency graph is displayed
        # Assert: The 'API Gateway' node is visible in the service dependency graph.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0)).to_contain_text("API Gateway", timeout=15000), "The 'API Gateway' node is visible in the service dependency graph."
        # Assert: The 'Payment Service' node is visible in the service dependency graph.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0)).to_contain_text("Payment Service", timeout=15000), "The 'Payment Service' node is visible in the service dependency graph."
        # Assert: The 'Order DB' node is visible in the service dependency graph.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0)).to_contain_text("Order DB", timeout=15000), "The 'Order DB' node is visible in the service dependency graph."
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
    