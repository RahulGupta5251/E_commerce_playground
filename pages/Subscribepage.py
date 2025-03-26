from pages.Basepage import Basepage


class Subscribepage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    newsletter_subscripton_msg_xpath = "(//*[text() = 'Newsletter Subscription'])[2]"
    newsletter_yes_radiobutton_xpath = "//*[@id='content']/form/fieldset/div/div/div[1]/label"
    newsletter_no_radiobutton_xpath = "//*[@id='content']/form/fieldset/div/div/div[2]/label"
    news_letter_continue_btn_xpath = "//*[@value = 'Continue']"

    def validate_newsletter_subscripton_msg_xpath(self):
        expected_text = "Newsletter Subscription"
        actual_text = self.get_element("newsletter_subscripton_msg_xpath",self.newsletter_subscripton_msg_xpath).text
        assert  expected_text == actual_text

    def click_yes_radio_button(self):
        self.click_on_element("newsletter_yes_radiobutton_xpath",self.newsletter_yes_radiobutton_xpath)

    def click_continue_btn_subscribepage(self):
        self.click_on_element("news_letter_continue_btn_xpath",self.news_letter_continue_btn_xpath)

