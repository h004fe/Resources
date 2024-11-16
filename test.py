import asyncio
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

async def main():
    args = ["--start-maximized"]
    browser: Browser = await launch(args=args)
    page: Page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 1000})
    await page.goto("https://google.com")

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )
    print(dimensions)
    await browser.close()

if __name__ == "__main__":
    asyncio.new_event_loop().run_until_complete(main())
