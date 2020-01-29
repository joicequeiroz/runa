from framework.webapp import WebBrowser
from maps.payroll_map import PayrollMap
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class PayrollPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.payroll_map = PayrollMap()

    def menu_payroll(self):
        self.click_on(self.payroll_map.payroll_menu)
        self.TakeScreenshot('Payroll Menu')

    def close_video(self):
        time.sleep(4)
        self.click_on(self.payroll_map.close_video)
        self.TakeScreenshot('closed video')

    def click_new(self):
        time.sleep(4)
        self.click_on(self.payroll_map.btn_new)
        self.TakeScreenshot('click_new')

    def group(self):
        time.sleep(4)
        self.click_on(self.payroll_map.group)
        time.sleep(2)
        self.send_keys(self.payroll_map.group, "Grupo 2")
        time.sleep(2)
        self.send_keys(self.payroll_map.group, Keys.ENTER)
        time.sleep(2)
        self.TakeScreenshot('select group')


    # def startdate(self, date):
    #     self.click_new(self.payroll_map.startdate, date)
    #     import pandas as pd
    #     data_frame = data_frame.set_index('date')
    #     df = data_frame[(data_frame.index > '31/05/2019') & (data_frame.index <= '06/06/2019')]
