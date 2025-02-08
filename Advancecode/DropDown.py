import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

class Dropdown_element():
    def dropdowntest(self):
        driver.get("https://demo.automationtesting.in/Register.html")
        # Find the Skills dropdown
        skills_dropdown = driver.find_element(By.ID, "Skills")
        select = Select(skills_dropdown)  # Initialize Select object with the dropdown element
        select.select_by_visible_text("Android")  # Select "Android" from the dropdown
        time.sleep(2)
        select.select_by_index(1)
        time.sleep(2)
        select.select_by_value("AutoCAD")
        time.sleep(2)
        # driver.quit()
test = Dropdown_element()
test.dropdowntest()

class checkbox():
    def checkbox_click(self):
        driver.get("https://demo.automationtesting.in/Register.html")
        checkbox1 = driver.find_element(By.ID, "checkbox1").click()

        time.sleep(2)
        # if not checkbox1.is_selected():
        #     checkbox1.click()

test1 = checkbox()
test1.checkbox_click()








