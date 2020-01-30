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
        close = self.driver.find_elements_by_xpath(self.payroll_map.close_video)
        close = close[-1]
        close.click()
        time.sleep(2)
        self.TakeScreenshot('closed video')

    def click_new(self):
        time.sleep(4)
        self.click_on(self.payroll_map.btn_new)
        self.TakeScreenshot('click_new')

    def group(self):
        time.sleep(4)
        self.send_keys(self.payroll_map.group, "Grupo 1")
        time.sleep(2)
        self.send_multiple_keys(self.payroll_map.group, [Keys.TAB, Keys.TAB, "01/06/2019", Keys.ENTER, Keys.TAB, "31/05/2019", Keys.TAB])
        time.sleep(2)
        # self.send_multiple_keys(self.payroll_map.startdate_incidence, ["31/05/2019", Keys.TAB])
        # time.sleep(2)
        # self.send_multiple_keys(self.payroll_map.enddate_incidence, ["06/06/2019", Keys.TAB])
        self.click_on(self.payroll_map.btn_sub)
        self.TakeScreenshot('select group')

    # def startdate(self, date):
    #     time.sleep(4)
    #     date = self.driver.find_elements_by_xpath("//*[@id='start_date']/input[value='01/06/2019']")
    #     date.click()
        # self.execute_script("arguments[0].value='01/06/2019';", date)
        # self.send_keys(self.payroll_map.startdate, "01/06/2019")
        # time.sleep(2)
        # self.send_keys(self.payroll_map.input_startate, Keys.TAB)
        # time.sleep(2)
        # self.send_keys(self.payroll_map.input_startate, Keys.TAB)
        # time.sleep(2)
        # self.TakeScreenshot('select startdate')
        # self.click_on(self.payroll_map.year)
        # self.click_on(self.payroll_map.select_year)
        # self.click_on(self.payroll_map.prev_month)
        # data_frame = data_frame.set_index('date')
        # df = data_frame[(data_frame.index > '31/05/2019') & (data_frame.index <= '06/06/2019')]
