import time
from datetime import datetime

import pytest

from pages.Accountpage import Accountpage
from pages.Basepage import Basepage
from pages.Loginpage import Loginpage
from pages.Registerpage import Registerpage
from pages.Successpage import Successpage


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Register:

    def generate_email(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rahulgupta"+time_stamp+"@gmail.com"

    def test_register_with_mandateory_credentials(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_register_button()
        register_page = Registerpage(self.driver)
        register_page.enter_first_name("Rahul....")
        register_page.enter_last_name("Gupta....")
        register_page.enter_email(self.generate_email())
        register_page.enter_telephone("7011996353")
        register_page.enter_password("Rahul221@")
        register_page.enter_confirm_password("Rahul221@")
        register_page.click_privacy_policy_checkbox()
        register_page.click_continue()
        expected_my_account_sucess_msg = "Congratulations! Your new account has been successfully created!"
        success_page = Successpage(self.driver)
        success_page.retrieve_success_msg_text().__eq__(expected_my_account_sucess_msg)


    def test_register_with_all_fields_credentials(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_register_button()
        register_page = Registerpage(self.driver)
        register_page.enter_first_name("Rahul....")
        register_page.enter_last_name("Gupta....")
        register_page.enter_email(self.generate_email())
        register_page.enter_telephone("7011996353")
        register_page.enter_password("Rahul221@")
        register_page.enter_confirm_password("Rahul221@")
        register_page.click_subscribe_button()
        register_page.click_privacy_policy_checkbox()
        register_page.click_continue()
        expected_my_account_sucess_msg = "Congratulations! Your new account has been successfully created!"
        success_page = Successpage(self.driver)
        success_page.retrieve_success_msg_text().__eq__(expected_my_account_sucess_msg)