from behave import when, then
from pages.login_page import LoginPage


@when(u'I do the invalid login with credentials "{email}" and "{password}"')
def step_impl_invalid_login(context, email, password):
    login_page = LoginPage(context)
    login_page.login(email, password)


@then(u'Then I should be see the following "{message}"')
def step_impl_is_user_not_logged(context, message):
    login_page = LoginPage(context)
    assert not login_page.is_logged(message)
