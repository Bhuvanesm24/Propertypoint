'''
Mouse Hover >> action.move_to_element(element1).move_to_element(element 2).click().perform()
Double click
Right CLick


'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# # Mouse Hover
# driver = webdriver.Chrome()  # Update path to your chromedriver
# driver.maximize_window()
# driver.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage")
# job = driver.find_element(By.XPATH, "//*[text()='Jobs']")
# IT_jobs = driver.find_element(By.XPATH, "//*[text()='IT jobs']")
# action=ActionChains(driver)
# action.move_to_element(job).move_to_element(IT_jobs).click().perform()
# driver.quit()

# Right Click
# driver = webdriver.Chrome()  # Update path to your chromedriver
# driver.maximize_window()
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")
# rightclick = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//*[text()='right click me']")
# rightclick.context_click(element).perform()
# alert = driver.find_element(By.XPATH,"//*[text()='Copy']").click()
# alerthandle = driver.switch_to.alert
# print(alerthandle.text)
# alerthandle.accept()

# Double click

# driver = webdriver.Chrome()  # Update path to your chromedriver
# driver.maximize_window()
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")
# doubleclick = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//*[text()='Double-Click Me To See Alert']")
# doubleclick.double_click(element).perform()
# alerthandle = driver.switch_to.alert
# print(alerthandle.text)
# alerthandle.accept()

# Click and hold, Drag and drop

driver = webdriver.Chrome()  # Update path to your chromedriver
driver.maximize_window()
driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")
driver.execute_script("window.scrollBy(0, 500);")
action = ActionChains(driver)

B = driver.find_element(By.XPATH, "//li[@name='B']")
A = driver.find_element(By.XPATH, "//li[@name='A']")
action.click_and_hold(B).move_to_element(A).release().perform()
time.sleep(3)

# wait = WebDriverWait(driver, 10)
