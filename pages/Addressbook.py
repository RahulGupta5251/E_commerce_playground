from selenium.webdriver.support.select import Select
from pages.Basepage import Basepage


class Addressbook(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    new_addess_button_xpath = "//*[text() = 'New Address']"

    add_address_first_name_xpath = "//*[@name = 'firstname']"
    add_address_lastname_xpath = "//*[@name = 'lastname']"
    add_address_company_name_xpath = "//*[@name = 'company']"
    add_address_address_1_xpath = "//*[@name = 'address_1']"
    add_address_address_2_xpath = "//*[@name = 'address_2']"
    add_address_city_xpath = "//*[@name = 'city']"
    add_address_postal_code_xpath = "//*[@name = 'postcode']"
    add_address_country_xpath = "//*[@name = 'country_id']"
    add_address_region_state_xpath = "//*[@name = 'zone_id']"

    add_address_no_radiobutton_xpath = "//*[@id='content']/form/fieldset/div[10]/div/div[2]/label/input"
    add_address_yes_radiobutton_xpath = "//*[@id='content']/form/fieldset/div[10]/div/div[1]/label/input"
    add_address_continue_xpath = "//*[@value = 'Continue']"


    def click_new_addressbutton(self):
        self.click_on_element("new_addess_button_xpath",self.new_addess_button_xpath)

    def add_new_address_details(self,firstname_value,lastname_value,companyname_value,addressvalue1,addressvalue2,cityvalue,pincode_value):
        self.type_to_element(firstname_value,"add_address_first_name_xpath",self.add_address_first_name_xpath)
        self.type_to_element(lastname_value,"add_address_lastname_xpath",self.add_address_lastname_xpath)
        self.type_to_element(companyname_value,"add_address_company_name_xpath",self.add_address_company_name_xpath)
        self.type_to_element(addressvalue1,"add_address_address_1_xpath",self.add_address_address_1_xpath)
        self.type_to_element(addressvalue2,"add_address_address_2_xpath",self.add_address_address_2_xpath)
        self.type_to_element(cityvalue,"add_address_city_xpath",self.add_address_city_xpath)
        self.type_to_element(pincode_value,"add_address_postal_code_xpath",self.add_address_postal_code_xpath)
        self.click_on_element("add_address_yes_radiobutton_xpath",self.add_address_yes_radiobutton_xpath)
    def select_country_dropdown(self):
        element = self.get_element("add_address_country_xpath",self.add_address_country_xpath)
        opt =Select(element)
        opt.select_by_visible_text("India")

    def select_state_dropdown(self):
        element = self.get_element("add_address_region_state_xpath",self.add_address_region_state_xpath)
        opt =Select(element)
        opt.select_by_visible_text("Delhi")
    def click_continue_addressbook_button(self):
        self.click_on_element("add_address_continue_xpath",self.add_address_continue_xpath)


