import pytest

from pages.Accountpage import Accountpage
from pages.Loginpage import Loginpage
from pages.Wishlistpage import Wishlistpage

@pytest.mark.usefixtures("setup_and_teardown")
class Testwishlist:

    def test_wishlist(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        account_page = Accountpage(self.driver)
        account_page.click_modify_wish_list()
        wishlist_page = Wishlistpage(self.driver)
        expected_wishlist_text = "My Wish List"
        wishlist_page.mywish_list_text().__eq__(expected_wishlist_text)
        wishlist_page.click_continue_button_wishlist()
