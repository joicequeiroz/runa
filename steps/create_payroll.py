from behave import when, then
from pages.payroll_page import PayrollPage


@when(u'I want to create a new Payroll')
def step_impl_create_payroll(context):
    payroll_page = PayrollPage(context)
    payroll_page.menu_payroll()
    payroll_page.close_video()
    payroll_page.click_new()


@when(u'I fill in required fields')
def step_impl_fill_in(context):
    payroll_page = PayrollPage(context)
    payroll_page.fill_in_payroll()


@then(u'the payroll should be generated automatically')
def step_impl_assert(context):
    payroll_page = PayrollPage(context)
    assert payroll_page.is_created()
    # payroll_page.click_start()
    # assert payroll_page.check_list()
    # payroll_page.click_delete()
