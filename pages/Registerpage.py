from datetime import datetime

from pages.Basepage import Basepage


class Registerpage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_xpath = "//*[@id='input-firstname']"
    last_name_xpath = "//*[@id='input-lastname']"
    email_filled_xpath = "//*[@id='input-email']"
    telephone_xpath = "//*[@id='input-telephone']"
    password_xpath = "//*[@id='input-password']"
    confirm_password_xpath = "//*[@id='input-confirm']"
    subscribe_yes_radio_button_xpath = "//label[@for='input-newsletter-yes']"
    privacy_policy_xpath = "//*[@id='content']/form/div/div/div/label"
    msg_enter_valid_phone_present_xpath = "//*[@id='input-telephone-help']"
    continue_button_xpath = "//*[@id='content']/form/div/div/input"
    warning_msg_xpath = "//*[@id='account-register']/div[1]/text()"

    def generate_email(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rahulgupta"+time_stamp+"@gmail.com"

    def enter_first_name(self,first_name_value):
        self.type_to_element(first_name_value,"first_name_xpath",self.first_name_xpath)

    def enter_last_name(self,last_name_value):
        self.type_to_element(last_name_value,"last_name_xpath",self.last_name_xpath)

    def enter_email(self,email_value):
        self.type_to_element(email_value,"email_filled_xpath",self.email_filled_xpath)

    def enter_telephone(self,phone_value):
        self.type_to_element(phone_value,"telephone_xpath",self.telephone_xpath)

    def enter_password(self,password_value):
        self.type_to_element(password_value,"password_xpath",self.password_xpath)

    def enter_confirm_password(self,confirm_password_value):
        self.type_to_element(confirm_password_value,"confirm_password_xpath",self.confirm_password_xpath)

    def click_subscribe_button(self):
        self.click_on_element("subscribe_yes_radio_button_xpath",self.subscribe_yes_radio_button_xpath)

    def click_privacy_policy_checkbox(self):
        self.click_on_element("privacy_policy_xpath",self.privacy_policy_xpath)

    def click_continue(self):
        self.click_on_element("continue_button_xpath",self.continue_button_xpath)

