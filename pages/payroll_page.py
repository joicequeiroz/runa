from framework.webapp import WebBrowser
from maps.payroll_map import PayrollMap
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PayrollPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.payroll_map = PayrollMap()

    def menu_payroll(self):
        self.click_on(self.payroll_map.payroll_menu)
        self.TakeScreenshot('Payroll Menu')

    def close_video(self):
        iframe = self.find_element_by_tag('_hjRemoteVarsFrame')
        self.switch_to.frame(iframe)
        self.click_on(self.payroll_map.close_video)

    def click_new(self):
        self.click_new(self.payroll_map.btn_new)

    def group(self, group):
        self.click_on(self.payroll_map.group, group)
        self.select_element_by_visible_text("Grupo 1")

    # def startdate(self, date):
    #     self.click_new(self.payroll_map.startdate, date)
    #     import pandas as pd
    #     data_frame = data_frame.set_index('date')
    #     df = data_frame[(data_frame.index > '31/05/2019') & (data_frame.index <= '06/06/2019')]
