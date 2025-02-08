import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)
webpagetile = driver.title
print (webpagetile)
expect_title = "Your Storel"
try:
    assert webpagetile == expect_title
    print("pass")
except Exception as e:
    print("fail")
