from selenium.webdriver.common.by import By


class Accountpage:

    def __init__(self,driver):
        self.driver = driver

    my_account_success_xpath = "//*[@id='content']/div[1]/h2"

    def retrive_my_account_success_element(self):
        return self.driver.find_element(By.XPATH,self.my_account_success_xpath).text