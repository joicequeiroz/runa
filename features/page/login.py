# import time

# from selenium import webdriver


# class LoginIn:
#     base_
#     user = 'producto+automation@runahr.com'
#     password = 'runahr'

#     def __init__(self, driver):
#         self.EMAIL = (By.ID, "email")
#         self.PASS = (By.ID, "password")
#         self.SUBMIT = (By.CLASS_NAME, "button.is-submit")
#         self.RESULT = (By.CSS_SELECTOR, "h1.title.inline.top")
        
#     def login(self, email, password):
#         context.web.find_element(*self.EMAIL).send_keys(user)
#         context.web.find_element(*self.PASS).send_keys(password)
#         context.web.find_element(*self.SUBMIT).click()
    
#     def validate(self, value):
#         element_hello = context.web.find_element(*self.RESULT)
#         assert value in element_hello.text

# context.web.get("http://automation.runademos.info/")
# driver.implicitly_wait(30)
# access = LoginIn(driver)
# access.login(user, password)
# access.value("¡Bienvenido, Administrador!")
