import time

import pytest
from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Application_Form_Framework.Form_Data import Form_Data_class
from Application_Form_Framework.Form_POM import FORM_POM


@pytest.mark.usefixtures("setup2")
class Test_Form:

    def test_TC1(self, form_data_set):
        self.driver.find_element(By.NAME, "firstname").send_keys(form_data_set["First_name"])
        self.driver.find_element(By.NAME, "lastname").send_keys(form_data_set["Last_name"])
        time.sleep(2)
        # Form_POM_Obj = FORM_POM(self.driver)
        # Form_POM_Obj.Name_Field().send_keys(form_data_set["First_name"])  # The field value should be data driven
        # Form_POM_Obj.Last_Name_Field().send_keys(form_data_set["Last_name"])  # The field value should be data driven


    def test_TC2(self):
        Gender_List = self.driver.find_elements(By.NAME, "sex")

        for gender in Gender_List:
            if gender.get_attribute("value") == "Male":
                gender.click()


    def test_TC3(self):
        Experience_List = self.driver.find_elements(By.NAME, "exp")

        for experience in Experience_List:
            if experience.get_attribute("id") == "exp-0":
                experience.click()
        time.sleep(3)

    def test_TC4(self):
        self.driver.find_element(By.ID, "datepicker").send_keys("22/04/1999")

        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(5)

    def test_TC5(self):
        Profession_List = self.driver.find_elements(By.NAME, "profession")

        print(len(Profession_List))

        for Profession in Profession_List:
            Profession.click()

        time.sleep(2)

        Tool_List = self.driver.find_elements(By.NAME, "tool")

        for Tools in Tool_List:
            Tools.click()

        time.sleep(2)

    def test_TC6(self):
        self.driver.find_element(By.ID, "continents").click()

        Select_Option = Select(self.driver.find_element(By.ID, "continents"))

        Select_Option.select_by_visible_text("Africa")
        time.sleep(3)
        self.driver.find_element(By.ID, "continents").click()
        time.sleep(2)

    def test_TC7(self):
        Selenium_Options = Select(self.driver.find_element(By.ID, "selenium_commands"))

        Selenium_Options.select_by_visible_text("Navigation Commands")
        time.sleep(5)

    def test_TC8(self):
        # driver.find_element(By.ID, "photo").send_keys("C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot 2024-07-05 175833.png")
        # time.sleep(5)

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, "photo")).click().perform()
        time.sleep(3)
        Key_Controller = Controller()
        Key_Controller.type("C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot 2024-07-05 175833.png")
        Key_Controller.press(Key.enter)
        Key_Controller.release(Key.enter)
        time.sleep(5)



@pytest.fixture(params = Form_Data_class.data)
def form_data_set(request):
    return request.param
