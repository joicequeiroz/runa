from selenium.webdriver.common.by import By


class LoginMap:
    # locators
    login_field = (By.ID, "#email")
    password_field = (By.ID, "#password")
    login_button = (By.CLASS_NAME, 'button.is-submit')
    login_message = (By.XPATH, "//h1[contains(.,'¡Bienvenido, Administrador!')]")
