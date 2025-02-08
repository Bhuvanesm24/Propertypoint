from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.myaccount_button = (By.XPATH, "//span[normalize-space()='My Account']")
        self.login_option = (By.XPATH, "//a[normalize-space()='Login']")
        self.register_option = (By.LINK_TEXT, "Register")
        self.search_field = (By.NAME, "search")
        self.webpage_logo = (By.XPATH, "//a[normalize-space()='Qafox.com']")
    def click_on_myaccount(self):
        self.driver.find_element(*self.myaccount_button).click()
    def select_login_option(self):
        self.driver.find_element(*self.login_option).click()
    def Click_on_resister_button(self):
        self.driver.find_element(*self.register_option).click()
    def Click_on_search_option(self):
        self.driver.find_element(*self.search_field).send_keys()
    def Verifiy_webpage_logo(self):
        self.driver.find_element(*self.webpage_logo).is_displayed()