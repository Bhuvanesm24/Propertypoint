from behave import *
from pages.Account_Page import AccountPage
from pages.Home_page import HomePage
from pages.Login_page import LoginPage
@given(u'Navigate to login page')
def step_impl(context):
    # context.driver.get("https://tutorialsninja.com/demo")
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_myaccount()
    context.home_page.select_login_option()
@when(u'Enter the valid user name as "{email}"')
def step_impl(context, email):
    context.login_page = LoginPage(context.driver)
    context.login_page.select_email_option(email)
@when(u'Enter the valid password as "{password}"')
def step_impl(context, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.select_password_option(password)
@when(u'Click on login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_login_button()
@then(u'Moving to login page')
def step_impl(context):
    context.myaccountpage = AccountPage(context.driver)
    assert context.myaccountpage.is_my_account_textisdisplayed()
@when(u'Enter the Invalid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.Enter_invalid_password()
@then(u'Error message should be displayed')
def step_impl(context):
    context.myaccountpage = AccountPage(context.driver)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password"
    assert context.myaccountpage.Display_proper_error_message(expected_warning_message)
@when(u'Enter the Invalid user name')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.Enter_invalid_emai_id()
