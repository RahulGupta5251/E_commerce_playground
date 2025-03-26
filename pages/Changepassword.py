from pages.Basepage import Basepage


class Changepassword(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    change_password_xpath = "//*[@id='input-password']"
    change_confirm_password_xpath = "//*[@id='input-confirm']"
    change_password_continue_xpath = "//*[@value = 'Continue']"

    def enter_change_passowrd(self,value):
        self.type_to_element(value,"change_password_xpath",self.change_password_xpath)

    def enter_change_confirm_passowrd(self, value):
        self.type_to_element(value, "change_confirm_password_xpath", self.change_confirm_password_xpath)

    def click_continue_button_change_password(self):
        self.click_on_element("change_password_continue_xpath",self.change_password_continue_xpath)
