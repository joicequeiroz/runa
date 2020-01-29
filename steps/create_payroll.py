from behave import when, then
from pages.payroll_page import PayrollPage


@when(u'I want to create a new Payroll')
def step_impl_create_payroll(context):
    payroll_page = PayrollPage(context)
    payroll_page.menu_payroll()
    payroll_page.close_video()
    payroll_page.click_new()


@when(u'I find the payroll group assigned to me')
def step_impl_get_group(context):
    payroll_page = PayrollPage(context)
    payroll_page.group()


@when(u'I inform the stardate')
def step_impl_insert_startdate(context):
    payroll_page = PayrollPage(context)
    payroll_page.group()


@then(u'the payroll should be generated automatically')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the payroll should be generated automatically')
