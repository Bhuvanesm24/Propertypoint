import os

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import Readconfiguration

def before_scenario(context, scenario):
    browser_name = Readconfiguration.read_configuration(category="Basic info", key="Browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(Readconfiguration.read_configuration(category="Basic info", key="url"))

def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png,
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)