import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.fedcm.account import Account

from pages.Accountpage import Accountpage
from pages.Loginpage import Loginpage


@pytest.mark.usefixtures("setup_and_teardown")
class Test_login:


    def test_login_with_valid_credentials(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        expected_success_text = "My Account"
        account_page = Accountpage(self.driver)
        account_page.retrive_my_account_success_element().__eq__(expected_success_text)

    def test_login_with_valid_email_and_invalid_password(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.select_register_button()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","1234567890")
        expected_warning_failed_msg = " Warning: No match for E-Mail Address and/or Password."
        login_page.retrive_failed_login_msg_element().__eq__(expected_warning_failed_msg)


    def test_login_with_invalid_email_and_valid_password(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.select_register_button()
        login_page.enter_login_credentials("51@gmail.com","Rahul221@")
        expected_warning_failed_msg = " Warning: No match for E-Mail Address and/or Password."
        login_page.retrive_failed_login_msg_element().__eq__(expected_warning_failed_msg)
