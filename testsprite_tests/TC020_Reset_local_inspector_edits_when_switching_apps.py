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
        
        # -> Click the 'API Gateway' node on the canvas to open the Node Inspector and view its editable fields.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> Edit the node name in the inspector to 'API Gateway (edited)', then switch to the 'Analytics Pipeline' application from the Apps list.
        # text field
        elem = page.locator('[id="node-name"]')
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("API Gateway (edited)")
        
        # -> Edit the node name in the inspector to 'API Gateway (edited)', then switch to the 'Analytics Pipeline' application from the Apps list.
        # Analytics Pipeline Real-time event processing button
        elem = page.get_by_role('button', name='Analytics Pipeline Real-time event processing', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the 'Checkout Service' entry in the Apps list to switch back to the original application so the API Gateway node can be inspected.
        # Checkout Service E-commerce checkout flow button
        elem = page.get_by_role('button', name='Checkout Service E-commerce checkout flow', exact=True)
        await elem.click(timeout=10000)
        
        # -> click
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # -> Select the 'API Gateway' node on the canvas and verify the Node name field reads 'API Gateway' in the Node Inspector.
        # API Gateway Routes incoming checkout requests
        elem = page.get_by_role('group', name='API Gateway Routes incoming checkout requests', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify the original node details are restored
        # Assert: Node Inspector 'Node name' input shows the original name 'API Gateway'.
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[1]/input").nth(0)).to_have_value("API Gateway", timeout=15000), "Node Inspector 'Node name' input shows the original name 'API Gateway'."
        # Assert: Node Inspector 'Description' shows the original description 'Routes incoming checkout requests'.
        await expect(page.locator("xpath=/html/body/div/div/div/aside/div/div[3]/div[2]/div[2]/div[2]/div[2]/textarea").nth(0)).to_have_text("Routes incoming checkout requests", timeout=15000), "Node Inspector 'Description' shows the original description 'Routes incoming checkout requests'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    