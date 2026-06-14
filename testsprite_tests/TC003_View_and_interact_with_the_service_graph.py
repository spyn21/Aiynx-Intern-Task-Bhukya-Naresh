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
        
        # -> Verify the graph nodes and edges are visible, then focus the canvas and attempt to pan using PageDown, zoom in and out using the 'Zoom In' and 'Zoom Out' buttons, and finally click the 'Fit View' button to restore the graph to the viewport.
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Verify the graph nodes and edges are visible, then focus the canvas and attempt to pan using PageDown, zoom in and out using the 'Zoom In' and 'Zoom Out' buttons, and finally click the 'Fit View' button to restore the graph to the viewport.
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Verify the graph nodes and edges are visible, then focus the canvas and attempt to pan using PageDown, zoom in and out using the 'Zoom In' and 'Zoom Out' buttons, and finally click the 'Fit View' button to restore the graph to the viewport.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit' button in the top-right of the canvas toolbar to restore the graph to the viewport, then wait briefly for the UI to settle and confirm that the nodes and edges remain visible.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify graph nodes and edges are displayed
        # Assert: The 'API Gateway' node and its description are visible.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0)).to_contain_text("API Gateway\nRoutes incoming checkout requests", timeout=15000), "The 'API Gateway' node and its description are visible."
        # Assert: The 'Payment Service' node and its description are visible.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0)).to_contain_text("Payment Service\nProcesses card and wallet payments", timeout=15000), "The 'Payment Service' node and its description are visible."
        # Assert: The 'Order DB' node and its description are visible.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0)).to_contain_text("Order DB\nPersists order records", timeout=15000), "The 'Order DB' node and its description are visible."
        
        # --> Verify the graph remains visible in the viewport
        await page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The 'API Gateway' graph node is visible in the viewport.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0)).to_be_visible(timeout=15000), "The 'API Gateway' graph node is visible in the viewport."
        await page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0).scroll_into_view_if_needed()
        # Assert: The 'Payment Service' graph node is visible in the viewport.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[2]").nth(0)).to_be_visible(timeout=15000), "The 'Payment Service' graph node is visible in the viewport."
        await page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0).scroll_into_view_if_needed()
        # Assert: The 'Order DB' graph node is visible in the viewport.
        await expect(page.locator("xpath=/html/body/div/div/div/main/div/div[1]/div/div/div[3]/div[3]").nth(0)).to_be_visible(timeout=15000), "The 'Order DB' graph node is visible in the viewport."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    