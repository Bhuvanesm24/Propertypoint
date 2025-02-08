from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Update path to your chromedriver
driver.maximize_window()
driver.get("https://www.rediff.com/")
driver.switch_to.frame("moneyiframe")
BSE = driver.find_element(By.ID, "bseindex")
print(BSE.text)
driver.switch_to.default_content()
Rediffmail = driver.find_element(By.XPATH,"//a[@class='linkcolor bold'][normalize-space()='Rediffmail']")
print(Rediffmail.text)
