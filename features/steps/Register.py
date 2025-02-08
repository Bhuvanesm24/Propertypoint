import time

from behave import *
from selenium.webdriver.common.by import By

from pages.Account_Page import AccountPage
from pages.Home_page import HomePage
from pages.Login_page import LoginPage
from pages.Register_Page import RegisterPage


@given(u'Navigate to register page')
def step_impl(context):
    context.home_page= HomePage(context.driver)
    context.home_page.click_on_myaccount()
    context.home_page.Click_on_resister_button()
@when(u'Enter details into mandatory field')
def step_impl(context ):
# def step_impl(context, firstname, lastname, mobilenumber, password, confrimpassword):
    for row in context.table:
        context.register_page = RegisterPage(context.driver)
        context.register_page.First_Name_filed(row["firstname"])
        context.register_page.Last_Name_filed(row["lastname"])
        context.register_page.EmailID_filed()
        context.register_page.MobileNumber_filed(row["mobilenumber"])
        context.register_page.Password_filed(row["password"])
        time.sleep(3)
        context.register_page.confirm_password_filed(row["confirmpassword"])
        time.sleep(3)
        context.register_page.Accept_and_Agree_filed()
        time.sleep(3)

@when(u'CLick on continue button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.Click_on_continue_button_for_login()
@then(u'Account should created')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.Accountshouldgenerated().is_displayed()

@when(u'Enter details into optional field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.Opptional_yes_should_selected()
@when(u'Enter details into all field expect email fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.First_Name_filed()
    context.register_page.Last_Name_filed()
    context.register_page.MobileNumber_filed()
    context.register_page.Password_filed()
    context.register_page.confirm_password_filed()
    context.register_page.Accept_and_Agree_filed()
@when(u'Enter details into existing email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.Enter_Existing_Email()
@then(u'Proper error message should displayed in duplicate email filed')
def step_impl(context):
    Expected_Error_messgae = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH,
    "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
        Expected_Error_messgae)

@when(u'Should not enter any fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then(u'Proper error message should displayed in all mandotary filed')
def step_impl(context):
    Firstname = "First Name must be between 1 and 32 characters!"
    assert context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'First Name must be between 1 and 32 characters!')]").text.__contains__(
        Firstname)
    Lastname = "Last Name must be between 1 and 32 characters!"
    Email = "E-Mail Address does not appear to be valid!"
    Telephone = "Telephone must be between 3 and 32 characters!"
    Password = "Password must be between 4 and 20 characters!"
    assert context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]").text.__contains__(
        Lastname)
    assert context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'E-Mail Address does not appear to be valid!')]").text.__contains__(
        Email)
    assert context.driver.find_element(By.XPATH,
                                       "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]").text.__contains__(
        Telephone)

