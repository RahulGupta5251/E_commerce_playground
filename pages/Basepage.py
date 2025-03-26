from selenium.webdriver.common.by import By


class Basepage:

    def __init__(self,driver):
        self.driver = driver


    def type_to_element(self,text, locator_name,locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_element(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def get_element(self,locator_name,locator_value):
        if locator_name.endswith("_xpath"):
           element =  self.driver.find_element(By.XPATH,locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME,locator_value)

        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_name.endswith("_classname"):
            element = self.driver.find_element(By.CLASS_NAME,locator_value)

        return element




