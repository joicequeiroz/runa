import time

from framework.webapp import WebBrowser
from maps.menu_map import MenuMap


class MenuPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.menu_map = MenuMap()

    def menu(self, menu):
        self.click_on(self.menu_map.payroll_menu)