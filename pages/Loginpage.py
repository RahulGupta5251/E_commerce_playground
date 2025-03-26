from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.Accountpage import Accountpage
from pages.Basepage import Basepage


class Loginpage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    my_account_xpath = "//*[@id='widget-navbar-217834']/ul/li[6]/a/div/span"
    register_button_xpath = "//*[@id='column-right']/div/a[2]"
    login_option_xpath = "//*[@id='widget-navbar-217834']/ul/li[6]/ul/li[1]/a"
    email_address_xpath = "//*[@id='input-email']"
    password_xpath = "//*[@id='input-password']"
    login_button_xpath = "//input[@type = 'submit']"
    warning_failed_msg_xpath = "//*[@id='account-login']/div[1]"

    def enter_my_account_menu(self):
        # act = ActionChains(self.driver)
        # element = self.get_element("my_account_xpath",self.my_account_xpath)
        # act.move_to_element(element)
        self.click_on_element("my_account_xpath",self.my_account_xpath)
        # self.driver.find_element(By.XPATH,self.my_account_xpath).click()

    def select_login_option(self):
        self.click_on_element("login_option_xpath",self.login_button_xpath)
        # self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def select_register_button(self):
        self.click_on_element("register_button_xpath",self.register_button_xpath)
        # self.driver.find_element(By.XPATH,self.register_xpath).click()

    def enter_email(self, email_value):
        self.type_to_element(email_value,"email_address_xpath",self.email_address_xpath)
        # self.driver.find_element(By.XPATH, self.email_address_xpath).send_keys(email_value)

    def enter_pasword(self, password_value):
        self.type_to_element(password_value, "password_xpath", self.password_xpath)
        # self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password_value)

    def enter_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return Accountpage(self.driver)

    def retrive_failed_login_msg_element(self):
        return self.driver.find_element(By.XPATH,self.warning_failed_msg_xpath).text

    def enter_login_credentials(self,email_value,password_value):
        self.enter_email(email_value)
        self.enter_pasword(password_value)
        self.enter_login()






