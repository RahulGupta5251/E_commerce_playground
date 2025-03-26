from datetime import time

import pytest

from pages.Accountpage import Accountpage
from pages.Addressbook import Addressbook
from pages.Basepage import Basepage
from pages.Loginpage import Loginpage

@pytest.mark.usefixtures("setup_and_teardown")
class TestAddressbook:

    def test_addressbook_add_new_address(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        account_page = Accountpage(self.driver)
        account_page.click_modify_adddress_book_button()
        address_book = Addressbook(self.driver)
        address_book.click_new_addressbutton()
        address_book.add_new_address_details("rahul...","gupta..","Samsung","karaeal nagar","sbs colony","Delhi","110094")
        address_book.select_country_dropdown()
        address_book.select_state_dropdown()
        address_book.click_continue_addressbook_button()



