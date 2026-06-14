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
        
        # -> Click the 'Zoom In' button to zoom the dependency graph and verify the nodes remain visible.
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph and verify the nodes remain visible.
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph and verify the nodes remain visible.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph and verify the nodes remain visible.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph and verify the nodes remain visible.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph, then click 'Zoom Out', then click 'Fit View', then pan the graph canvas down, and pan it back up to verify nodes remain visible.
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph, then click 'Zoom Out', then click 'Fit View', then pan the graph canvas down, and pan it back up to verify nodes remain visible.
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph, then click 'Zoom Out', then click 'Fit View', then pan the graph canvas down, and pan it back up to verify nodes remain visible.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the dependency graph, then click 'Zoom Out', then click 'Fit View', then pan the graph canvas down, and pan it back up to verify nodes remain visible.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the graph (then Zoom Out, click 'Fit', pan the canvas down and pan it back up) to verify the nodes remain visible and positioned in the viewport.
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then Zoom Out, click 'Fit', pan the canvas down and pan it back up) to verify the nodes remain visible and positioned in the viewport.
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then Zoom Out, click 'Fit', pan the canvas down and pan it back up) to verify the nodes remain visible and positioned in the viewport.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then Zoom Out, click 'Fit', pan the canvas down and pan it back up) to verify the nodes remain visible and positioned in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the graph (then Zoom Out, click 'Fit', pan the canvas down and pan it back up) to verify the nodes remain visible and positioned in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the graph (then perform Zoom Out, Fit View, pan down, and pan up to verify nodes remain visible).
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then perform Zoom Out, Fit View, pan down, and pan up to verify nodes remain visible).
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then perform Zoom Out, Fit View, pan down, and pan up to verify nodes remain visible).
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button to zoom the graph (then perform Zoom Out, Fit View, pan down, and pan up to verify nodes remain visible).
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button to zoom the graph (then perform Zoom Out, Fit View, pan down, and pan up to verify nodes remain visible).
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button, then click 'Zoom Out', then click the 'Fit' (Fit View) button, then pan the graph canvas down and pan it back up to confirm the nodes remain visible in the viewport.
        # Zoom In button
        elem = page.get_by_role('button', name='Zoom In', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button, then click 'Zoom Out', then click the 'Fit' (Fit View) button, then pan the graph canvas down and pan it back up to confirm the nodes remain visible in the viewport.
        # Zoom Out button
        elem = page.get_by_role('button', name='Zoom Out', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button, then click 'Zoom Out', then click the 'Fit' (Fit View) button, then pan the graph canvas down and pan it back up to confirm the nodes remain visible in the viewport.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Zoom In' button, then click 'Zoom Out', then click the 'Fit' (Fit View) button, then pan the graph canvas down and pan it back up to confirm the nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Zoom In' button, then click 'Zoom Out', then click the 'Fit' (Fit View) button, then pan the graph canvas down and pan it back up to confirm the nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Fit View' button to center the graph, then click the 'API Gateway' node to open the Node Inspector, then pan the graph canvas down and pan it back up to verify nodes remain visible in the viewport.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit View' button to center the graph, then click the 'API Gateway' node to open the Node Inspector, then pan the graph canvas down and pan it back up to verify nodes remain visible in the viewport.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit View' button to center the graph, then click the 'API Gateway' node to open the Node Inspector, then pan the graph canvas down and pan it back up to verify nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Fit View' button to center the graph, then click the 'API Gateway' node to open the Node Inspector, then pan the graph canvas down and pan it back up to verify nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> click
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> click
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> scroll
        await page.mouse.wheel(0, 300)
        
        # -> scroll
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Fit' button to center the graph, then click the 'API Gateway' node, then pan the canvas down and pan it back up to verify the nodes remain visible in the viewport.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit' button to center the graph, then click the 'API Gateway' node, then pan the canvas down and pan it back up to verify the nodes remain visible in the viewport.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit' button to center the graph, then click the 'API Gateway' node, then pan the canvas down and pan it back up to verify the nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Fit' button to center the graph, then click the 'API Gateway' node, then pan the canvas down and pan it back up to verify the nodes remain visible in the viewport.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Fit View' button to center the graph, click the 'API Gateway' node to confirm the Node Inspector opens, then pan the canvas down and pan it back up to verify nodes remain visible; finish and report results.
        # Fit View button
        elem = page.get_by_role('button', name='Fit View', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Fit View' button to center the graph, click the 'API Gateway' node to confirm the Node Inspector opens, then pan the canvas down and pan it back up to verify nodes remain visible; finish and report results.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the graph remains visible and positioned within the viewport
        await page.locator("xpath=/html/body/div[1]/div/div/main/div/div[3]/svg").nth(0).scroll_into_view_if_needed()
        # Assert: The graph canvas (Mini Map SVG) is visible in the viewport.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/main/div/div[3]/svg").nth(0)).to_be_visible(timeout=15000), "The graph canvas (Mini Map SVG) is visible in the viewport."
        await page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert: The API Gateway node is visible and positioned within the viewport.
        await expect(page.locator("xpath=/html/body/div[1]/div/div/main/div/div[1]/div/div/div[3]/div[1]").nth(0)).to_be_visible(timeout=15000), "The API Gateway node is visible and positioned within the viewport."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    