import time
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

class alteraccept():
    def alteracceptfield(self):
        driver.get("https://letcode.in/alert")
        driver.find_element(By.XPATH, "//button[@id='accept']").click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@id='confirm']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.dismiss()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@id='prompt']").click()
        alert = driver.switch_to.alert
        alert.send_keys("Buvanes")
        alert.accept()
        driver.save_screenshot("bhuvan.png")

test=alteraccept()
test.alteracceptfield()






















#
# class Alert_Testcase01():
#     def Simple_Alert(self):
#         driver.get("https://letcode.in/alert")
#         driver.find_element(By.ID, "accept").click()
#         Alert(driver).accept()
#         time.sleep(2)
#
# dd=Alert_Testcase01()
# dd.Simple_Alert()
#
# class Alert_Testcase02():
#     def Alert_accept(self):
#         driver.get("https://letcode.in/alert")
#         driver.find_element(By.ID, "confirm").click()
#         Alert(driver).accept()
#         time.sleep(2)
#
# dd2=Alert_Testcase02()
# dd2.Alert_accept()
#
# class Alter_Testcase03():
#     def Alter_dismiss(self):
#         driver.get("https://letcode.in/alert")
#         driver.find_element(By.ID, "confirm").click()
#         Alert(driver).dismiss()
#         time.sleep(3)
#
# dd3=Alter_Testcase03()
# dd3.Alter_dismiss()
#
# class Alter_Testcase04():
#     def Alter_Prompt(self):
#         driver.get("https://letcode.in/alert")
#         driver.find_element(By.ID, "prompt").click()
#         driver.switch_to.alert.send_keys("This is Bhuvanes")
#         time.sleep(3)
#         Alert(driver).accept()
#         time.sleep(3)
#
# dd3=Alter_Testcase04()
# dd3.Alter_Prompt()
#
#
#
#
#
