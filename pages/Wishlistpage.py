from pages.Basepage import Basepage


class Wishlistpage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    my_wish_list_text_xpath = "//*[text() = 'My Wish List']"
    wish_list_continue_button_xpath = "//*[text()= 'Continue']"


    def mywish_list_text(self):
        element =  self.get_element("my_wish_list_text_xpath",self.my_wish_list_text_xpath)
        return element.text

    def click_continue_button_wishlist(self):
        self.click_on_element("wish_list_continue_button_xpath",self.wish_list_continue_button_xpath)


