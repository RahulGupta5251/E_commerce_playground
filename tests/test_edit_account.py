import pytest

from pages.Accountpage import Accountpage
from pages.Editaccountpage import Editaccountpage
from pages.Loginpage import Loginpage

@pytest.mark.usefixtures("setup_and_teardown")
class Test_edit_account:

    def test_edit_account(self):
        login_page = Loginpage(self.driver)
        login_page.enter_my_account_menu()
        login_page.select_login_option()
        login_page.enter_login_credentials("Rahulgupta5251@gmail.com","Rahul221@")
        account_page = Accountpage(self.driver)
        account_page.click_edit_your_account_information()
        edit_account = Editaccountpage(self.driver)
        edit_account.edit_first_name("rahul")
        edit_account.edit_last_name("gupta")
        edit_account.edit_email_address("Rahulgupta5251@gmail.com")
        edit_account.edit_telephone("7011996353")
        edit_account.click_continue_button_editaccount()
        # edit_account_success_msg = " Success: Your account has been successfully updated."
        # account_page.retrive_edit_account_succees_msg_text().__eq__(edit_account_success_msg)