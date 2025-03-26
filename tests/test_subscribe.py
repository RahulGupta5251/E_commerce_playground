from pages.Accountpage import Accountpage
from pages.Loginpage import Loginpage
from pages.Subscribepage import Subscribepage
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class Test_subscribe:

    def test_subscribe(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        account_page = Accountpage(self.driver)
        account_page.click_subscribe_button()
        subscribe_page = Subscribepage(self.driver)
        subscribe_page.validate_newsletter_subscripton_msg_xpath()
        subscribe_page.click_yes_radio_button()
        subscribe_page.click_continue_btn_subscribepage()
