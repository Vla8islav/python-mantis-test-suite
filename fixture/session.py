from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user):
        # Login
        self.app.open_home_page()
        self.app.wd.find_element_by_name("username").clear()
        self.app.wd.find_element_by_name("username").send_keys(user.username)
        self.app.wd.find_element_by_css_selector("form[id=login-form] input[type=submit]").click()
        self.app.wd.find_element_by_name("password").clear()
        self.app.wd.find_element_by_name("password").send_keys(user.password)
        self.app.wd.find_element_by_css_selector("form[id=login-form] input[type=submit]").click()

    def ensure_login(self, user):
        if not self.are_we_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
            self.login(user)

    def logout(self):
        self.app.wd.delete_all_cookies()
        self.app.wd.refresh()

    def ensure_logout(self):
        if self.are_we_logged_in():
            self.logout()

    def are_we_logged_in(self):
        try:
            retval = len(self.app.wd.find_element_by_css_selector("span.user-info")) > 0
        except:
            retval = False
        return retval

    def is_logged_in_as(self, user):
        try:
            retval = self.app.wd.find_element_by_css_selector("span.user-info").text == user.username
        except NoSuchElementException:
            retval = False
        return retval
