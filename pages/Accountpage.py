from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class Accountpage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_information_xpath = "//*[text() = ' Edit your account information']"
    change_your_password_button_xpath = "//*[@id='content']/div[1]/div/div/div[2]/a"
    modify_your_addres_book_xpath = "//*[@id='content']/div[1]/div/div/div[3]/a"
    modify_your_wish_list_xpath = "//*[@id='content']/div[1]/div/div/div[4]/a"

    ##########Success x path ########
    my_account_success_xpath = "//*[@id='content']/div[1]/h2"
    edit_account_success_msg_xpath = "//*[@id='account-account']/div[1]"
    change_password_success_msg_xpath = "//*[text()= ' Success: Your password has been successfully updated.']"

    def retrive_my_account_success_element(self):
        return self.driver.find_element(By.XPATH,self.my_account_success_xpath).text

    def click_edit_your_account_information(self):
        self.click_on_element("edit_your_account_information_xpath",self.edit_your_account_information_xpath)
        # self.driver.find_element(By.XPATH,self.edit_your_account_information_xpath).click()

    def click_modify_adddress_book_button(self):
        self.click_on_element("modify_your_addres_book_xpath",self.modify_your_addres_book_xpath)

    def click_modify_wish_list(self):
        self.click_on_element("modify_your_wish_list_xpath",self.modify_your_wish_list_xpath)

    def click_change_your_password_btn(self):
        self.click_on_element("change_your_password_button_xpath",self.change_your_password_button_xpath)

    def retrive_edit_account_succees_msg_text(self):
        return self.get_element("edit_account_success_msg_xpath",self.edit_account_success_msg_xpath).text

    def change_password_success_msg_text(self):
        return self.get_element("change_password_success_msg_xpath",self.change_password_success_msg_xpath).text