from selenium.webdriver.common.by import By
class AccountPage():
    def __init__(self,driver):
        self.driver = driver
        self.Account_sucess_screen = (By.LINK_TEXT,"My Account")
        self.proper_error_message_should_be_displayed = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        self.profile_genarated_xpath = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    def is_my_account_textisdisplayed(self):
        return self.driver.find_element(*self.Account_sucess_screen).is_displayed()
    def Display_proper_error_message(self,expected_warning_message):
        return self.driver.find_element(*self.proper_error_message_should_be_displayed).text.__contains__(expected_warning_message)
    def Accountshouldgenerated(self):
        return self.driver.find_element(*self.profile_genarated_xpath).is_displayed()

