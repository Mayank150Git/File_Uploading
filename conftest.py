import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="chrome", help="The default value is chrome"
    )


@pytest.fixture(scope="class")
def setup2(request):
    browser = request.config.getoption("--browser_type")

    if browser == "chrome":
        Service_Object = Service()
        driver = webdriver.Chrome(service=Service_Object)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        assert driver.find_element(By.XPATH, "(//h3)[5]").text == "Demo Automation Practice Form"
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()

    elif browser == "firefox":
        Service_Object = Service()
        driver = webdriver.Firefox(service=Service_Object)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        assert driver.find_element(By.XPATH, "(//h3)[5]").text == "Demo Automation Practice Form"
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()

    elif browser == "ie":
        Service_Object = Service()
        driver = webdriver.Ie(service=Service_Object)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        assert driver.find_element(By.XPATH, "(//h3)[5]").text == "Demo Automation Practice Form"
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()



