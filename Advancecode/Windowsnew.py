from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Step 1: Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
parent = driver.current_window_handle
driver.find_element(By.XPATH, "//a[normalize-space()='Open a popup window']").click()
time.sleep(2)
child = driver.window_handles

for w in child:
    driver.switch_to.window(w)
    if driver.title.__eq__("New Window"):
        newwindowtext = driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text
        print(newwindowtext)
        break

