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
        close = self.driver.find_elements_by_xpath(
            self.payroll_map.close_video)
        close = close[-1]
        close.click()
        time.sleep(2)
        self.TakeScreenshot('closed video')

    def click_new(self):
        time.sleep(4)
        self.click_on(self.payroll_map.btn_new)
        self.TakeScreenshot('click_new')

    def set_date(self, element, date):
        time.sleep(2)
        cont = 0
        while (cont < 10):
            self.send_keys(element, date[cont])
            cont = cont + 1
        time.sleep(2)

    def fill_in_payroll(self):
        time.sleep(4)
        self.send_keys(self.payroll_map.group, "Grupo 1")
        time.sleep(2)
        self.send_multiple_keys(self.payroll_map.group,
                                [Keys.TAB, Keys.TAB, "01/06/2019", Keys.TAB])
        time.sleep(2)
        self.set_date(self.payroll_map.stardate_incidence, "31/05/2019")
        self.set_date(self.payroll_map.endate_incidence, "06/06/2019")
        self.click_on(self.payroll_map.btn_sub)
        time.sleep(5)
        self.TakeScreenshot('fill in payroll')

    def is_created(self):
        time.sleep(5)
        self.is_element_present("//button[contains(text(),'Comenzar')]")
        time.sleep(5)
        self.TakeScreenshot('created')
        return True

    def click_start(self):
        time.sleep(5)
        self.click_on(self.payroll_map.btn_start)

    def click_delete(self):
        time.sleep(10)
        self.click_on(self.payroll_map.btn_delete)
        time.sleep(5)
        self.click_on(self.payroll_map.btn_confirm_del)

    def click_continue(self):
        time.sleep(20)
        self.click_on(self.payroll_map.btn_continue)
