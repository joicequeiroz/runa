

class LoginMap:
    # locators
    login_field = "//input[@id='email']"
    password_field = "//input[@id='password']"
    login_button = "//button[contains(text(),'Ingresar')]"
    login_message = "//h1[contains(.,'¡Bienvenido, Administrador!')]"
    invalid_login = "//span[contains(.,'No se inició sesión. Verifique que la contraseña sea correcta')]"
