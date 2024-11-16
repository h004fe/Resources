import asyncio
from pyppeteer import launch

async def main():
 browser = await launch(headless=True, args=['--no-sandbox'])
 page = await browser.newPage()
 await page.goto('https://h004fe.github.io/Resources/test.html')
 
 dimensions = await page.evaluate(
    """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )
 await browser.close()
 print(dimensions)
 
asyncio.get_event_loop().run_until_complete(main())
