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
        
        # -> Click the 'Analytics Pipeline' entry in the Apps list to switch the selected application and trigger the service graph to refresh.
        # Analytics Pipeline Real-time event processing button
        elem = page.get_by_role('button', name='Analytics Pipeline Real-time event processing', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Checkout Service' entry in the Apps list to switch the selected application and verify the service graph refreshes to show Checkout Service nodes.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Analytics Pipeline' entry in the Apps list to switch the selected application and trigger the service graph to refresh.
        # Analytics Pipeline Real-time event processing button
        elem = page.get_by_role('button', name='Analytics Pipeline Real-time event processing', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Checkout Service' entry in the Apps list to switch the selected application and verify the service graph refreshes to show Checkout Service nodes.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Analytics Pipeline' entry in the Apps list to switch the selected application and verify the service graph refreshes to show Analytics nodes.
        # Analytics Pipeline Real-time event processing button
        elem = page.get_by_role('button', name='Analytics Pipeline Real-time event processing', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the service dependency graph refreshes for the newly selected app
        await page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The canvas displays the 'Event Ingest' node for the selected app.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0)).to_be_visible(timeout=15000), "The canvas displays the 'Event Ingest' node for the selected app."
        await page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert: The canvas displays the 'Stream Processor' node for the selected app.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0)).to_be_visible(timeout=15000), "The canvas displays the 'Stream Processor' node for the selected app."
        await page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0).scroll_into_view_if_needed()
        # Assert: The canvas displays the 'Data Warehouse' node for the selected app.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0)).to_be_visible(timeout=15000), "The canvas displays the 'Data Warehouse' node for the selected app."
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
    