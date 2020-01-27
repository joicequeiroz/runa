from behave import when, then
from pages.login_page import LoginPage


@when('I go to "{page}" page')
def step_impl_goto_page(context, page):
    login_page = LoginPage(context)
    import time
    time.sleep(2)


@when('I do the valid login with credentials "{email}" and "{password}"')
def step_impl_valid_login(context, email, password):
    login_page = LoginPage(context)
    login_page.login(email, password)


@then('I should be logged in')
def step_impl_is_user_logged(context):
    login_page = LoginPage(context)
    assert login_page.is_logged()
