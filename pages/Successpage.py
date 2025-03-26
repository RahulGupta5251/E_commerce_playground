from pages.Basepage import Basepage


class Successpage(Basepage):
    def __init__(selfself,driver):
        super().__init__(driver)

    account_success_msg_xpath = "//*[@id='content']/p[2]"

    def retrieve_success_msg_text(self):
        return self.get_element("account_success_msg_xpath",self.account_success_msg_xpath).text
