from behave import when, then

from pages.login_page import LoginPage

@when(u'I do the invalid login with credentials "{email}" and "{password}"')
def step_impl_invalid_login(context, email, password):
    login_page = LoginPage(context)
    login_page.login(email, password)


@then(u'I should not be logged in')
def step_impl_is_user_logged(context):
    login_page = LoginPage(context)
    assert not login_page.is_logged()
