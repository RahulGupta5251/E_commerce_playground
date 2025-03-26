from selenium import webdriver
import pytest

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
    yield driver
    driver.quit()
