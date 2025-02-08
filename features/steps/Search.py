from behave import *
from selenium.webdriver.common.by import By
from pages.Account_Page import AccountPage
from pages.Home_page import HomePage
from pages.Login_page import LoginPage
from pages.Register_Page import RegisterPage

@given(u'Navigate to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Navigate to home page')
@when(u'Enter the valid product into the search box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter the valid product into the search box')
@when(u'Click on search button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on search button')
@then(u'Valid product should displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Valid product should displayed')


@when(u'Enter the invalid product into the search box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter the invalid product into the search box')


@then(u'Proper error message should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper error message should be displayed')


@when(u'Search without entering the product name in search filed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Search without entering the product name in search filed')
