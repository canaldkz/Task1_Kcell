
class Page():
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url=url)

    def scroll_to_elem(self, element):
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);", element
        )
