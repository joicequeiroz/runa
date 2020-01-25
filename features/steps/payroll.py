from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# site
driver = webdriver.Chrome('C:\\Python38-32\\Scripts\\chromedriver.exe')
base_url = 'http://automation.runademos.info/'

# Variable to interact with the page
user = 'producto+automation@runahr.com'
password = 'runahr'
element_email = 'email'
element_password = 'password'
button_sub = 'button.is-submit'
element_hello = "//h1[contains(.,'¡Bienvenido, Administrador!')]"
payroll_menu = "//a[contains(.,'payroll')]"
btn_new = "button.button.is-light-green"
select_group = '.react-select__indicators'


@given('I have access to Runa RH as admin')
def step_impl(context):
    context.web.get(base_url + "/")
    EMAIL = (By.ID, element_email)
    PASS = (By.ID, element_password)
    SUBMIT = (By.CLASS_NAME, button_sub)
    RESULT = (By.XPATH, element_hello)

    def login(email, password):
        context.web.find_element(*EMAIL).send_keys(user)
        context.web.find_element(*PASS).send_keys(password)
        context.web.find_element(*SUBMIT).click()
    login(user, password)

    def validate(value):
        context.element_hello = context.web.find_element(*RESULT)
        assert "¡Bienvenido, Administrador!" in element_hello.text
    
@when('I want to create a new Payroll')
def step_impl(context):
    MENU_PAYROLL = (By.XPATH, payroll_menu)
    BTN_NEW = (By.CLASS_NAME, btn_new)

    def create_payroll(MENU_PAYROLL):
        element = context.web.find_elements(*MENU_PAYROLL)

        for x in element:

            if x.text == "nome do botao":
                x.click()

    create_payroll(MENU_PAYROLL)

    def new_payroll(BTN_NEW):
        element = context.web.find_elements(*BTN_NEW)

        for x in element:

            if x.text == "nome do botao":
                x.click()

    create_payroll(BTN_NEW)

@when('I find the payroll group assigned to me')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When I find the payroll group assigned to me')
    # for key, handle in enumerate(driver.current_window_handle):
    #     print(key, handle)
    #     print("Janela Atual: {}".format(driver.current_window_handle))
    driver.switch_to_window(driver.current_window_handle[1])
    # driver.switch_to.window("_blank")
    GROUP = (By.CSS_SELECTOR, select_group)
    def select_group(GROUP):
        element = context.web.find_elements(GROUP).click()

    select_group(GROUP)


@when('I inform the stardate')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I inform the stardate')


@then('the payroll should be generated automatically')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the payroll should be generated automatically')
