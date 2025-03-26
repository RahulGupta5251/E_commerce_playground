from pages.Basepage import Basepage


class Editaccountpage(Basepage):
    def __init__(self,driver):
        self.driver = driver


    edit_first_name_xpath = "//*[@id='input-firstname']"
    edit_last_name_xpath = "//*[@id='input-lastname']"
    edit_email_xpath = "//*[@id='input-email']"
    edit_telephone_xpath = "//*[@id='input-telephone']"
    edit_continue_xpath = "//*[@id='content']/form/div/div[2]/input"
    # = " Success: Your account has been successfully updated."

    def edit_first_name(self,text):
        self.type_to_element(text,"edit_first_name_xpath",self.edit_first_name_xpath)

    def edit_last_name(self, text):
        self.type_to_element(text, "edit_last_name_xpath", self.edit_last_name_xpath)

    def edit_email_address(self, text):
        self.type_to_element(text, "edit_email_xpath", self.edit_email_xpath)

    def edit_telephone(self, text):
        self.type_to_element(text, "edit_telephone_xpath", self.edit_telephone_xpath)

    def click_continue_button_editaccount(self):
        self.click_on_element( "edit_continue_xpath", self.edit_continue_xpath)

