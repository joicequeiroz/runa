from framework.webapp import WebBrowser
from maps.login_map import LoginMap


class AccessPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.login_map = LoginMap()

    def access(self, email, password):
        self.send_keys(self.login_map.login_field, "producto+automation@runahr.com")
        self.send_keys(self.login_map.password_field, "runahr")
        self.TakeScreenshot('Login')
        self.click_on(self.login_map.login_button)