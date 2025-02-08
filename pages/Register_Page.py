from datetime import datetime
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname_id = (By.ID,"input-firstname")
        self.lastname_id = (By.ID, "input-lastname")
        self.emailid_id = (By.ID,"input-email")
        self.mobilenumber_id =(By.ID, "input-telephone")
        self.password_id = (By.ID, "input-password")
        self.confirm_password_id = (By.ID,"input-confirm")
        self.acceptandagree_name =(By.NAME, "agree")
        self.login_button_xpath = (By.XPATH, "//input[@value='Continue']")
        self.opptional_YES_xpath = (By.XPATH, "//label[normalize-space()='Yes']")
        self.existing_emailid_id = (By.ID, "input-email")

    def First_Name_filed(self, firstname):
        self.driver.find_element(*self.firstname_id).send_keys(firstname)
    def Last_Name_filed(self,lastname):
        self.driver.find_element(*self.lastname_id).send_keys(lastname)
    def EmailID_filed(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_email = "bhuvi" + time_stamp + "@gmail.com"
        self.driver.find_element(*self.emailid_id).send_keys(new_email)
    def MobileNumber_filed(self, mobilenumber):
        self.driver.find_element(*self.mobilenumber_id).send_keys(mobilenumber)
    def Password_filed(self, password):
        self.driver.find_element(*self.password_id).send_keys(password)
    def confirm_password_filed(self, confirmpassword):
        self.driver.find_element(*self.confirm_password_id).send_keys(confirmpassword)
    def Accept_and_Agree_filed(self):
        self.driver.find_element(*self.acceptandagree_name).click()
    def Click_on_continue_button_for_login(self):
        self.driver.find_element(*self.login_button_xpath).click()

    def Opptional_yes_should_selected(self):
        self.driver.find_element(*self.opptional_YES_xpath).click()
    def Enter_Existing_Email(self, existingemail ):
        self.driver.find_element(*self.existing_emailid_id).send_keys(existingemail)