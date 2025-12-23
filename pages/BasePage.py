from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def wait_for_visible(self, element, timeout: int = 10000):
        element.wait_for(state="visible", timeout=timeout)



