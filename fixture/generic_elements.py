class GenericElementsHelper:

    def __init__(self, app):
        self.app = app

    def type(self, css_selector, text):
        if text is not None:
            self.app.wd.find_element_by_css_selector(css_selector).clear()
            self.app.wd.find_element_by_css_selector(css_selector).send_keys(text)
