import time

from framework.webapp import WebBrowser
from maps.login_map import LoginMap


class LoginPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.login_map = LoginMap()

    def login(self, email, password):
        self.send_keys(self.login_map.login_field, email)
        self.send_keys(self.login_map.password_field, password)
        self.TakeScreenshot('Login')
        self.click_on(self.login_map.login_button)

    def is_logged(self):
        message = self.wait_element(self.login_map.login_message, timeout=50)
        self.TakeScreenshot('Check it is logged')
        return "You logged into a Runa" in message.text
