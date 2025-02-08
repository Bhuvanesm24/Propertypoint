from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_address = (By.XPATH, "//input[@id='input-email']")
        self.password_field = (By.XPATH, "//input[@id='input-password']")
        self.login_button = (By.XPATH, "//input[@value='Login']")
        self.invalid_email_address = (By.XPATH, "//input[@id='input-email']")
        self.invali_password_field = (By.XPATH, "//input[@id='input-password']")

    def select_email_option(self, email):
        self.driver.find_element(*self.email_address).send_keys(email)

    def select_password_option(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.login_button).click()
    def Enter_invalid_emai_id(self):
        self.driver.find_element(*self.invalid_email_address).send_keys("ghyu@gmail.com")
    def Enter_invalid_password(self):
        self.driver.find_element(*self.invali_password_field).send_keys("123456789")