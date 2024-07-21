from selenium.webdriver.common.by import By


class FORM_POM:

    def __init__(self, driver):
        self.driver = driver


    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")

    def Name_Field(self):
        # self.driver.find_element(By.NAME, "firstname")
        return self.driver.find_element(*FORM_POM.FIRST_NAME)
    def Last_Name_Field(self):
        return self.driver.find_element(*FORM_POM.LAST_NAME)
