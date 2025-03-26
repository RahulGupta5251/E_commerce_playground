from pages.Accountpage import Accountpage
from pages.Changepassword import Changepassword
from pages.Loginpage import Loginpage
import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class Test_changepassword:

    def test_change_password(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        account_page = Accountpage(self.driver)
        account_page.click_change_your_password_btn()
        change_password = Changepassword(self.driver)
        change_password.enter_change_passowrd("Rahul221@")
        change_password.enter_change_confirm_passowrd("Rahul221@")
        change_password.click_continue_button_change_password()
        # expected_change_password_sucess_msg_text = " Success: Your password has been successfully updated."
        # assert account_page.change_password_success_msg_text().__eq__(expected_change_password_sucess_msg_text)