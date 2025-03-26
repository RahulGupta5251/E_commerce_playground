from select import select
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities import Readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = Readconfigurations.readconfigurations("basic_info","browser")
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif  browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        return "please select valid webdriver to launch.........."
    url = Readconfigurations.readconfigurations("basic_info","url")
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    # element = driver.find_element(By.XPATH,"sdjfhdsj")
    # opt = Select(element)
    # opt.se
    yield driver
    driver.quit()
