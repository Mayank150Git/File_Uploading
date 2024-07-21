import time

from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_Object = Service()
driver = webdriver.Chrome(service=Service_Object)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.implicitly_wait(5)
assert driver.find_element(By.XPATH, "(//h3)[5]").text == "Demo Automation Practice Form"  #TC1
driver.maximize_window()

#TC2: Fill name/last name

driver.find_element(By.NAME, "firstname").send_keys("Mayank Tripathi") #The field value should be data driven
driver.find_element(By.NAME, "lastname").send_keys("Tripathi") #The field value should be data driven

#TC3: Intraction with the Radio Button

Gender_List = driver.find_elements(By.NAME, "sex")

for gender in Gender_List:
    if gender.get_attribute("value") == "Male":
        gender.click()


#TC4: Selecting the Year of Exp

Experience_List = driver.find_elements(By.NAME, "exp")

for experience in Experience_List:
    if experience.get_attribute("id") == "exp-0":
        experience.click()

time.sleep(3)

#TC5: Entering the Data field value

driver.find_element(By.ID, "datepicker").send_keys("22/04/1999")

driver.execute_script("window.scrollTo(0,1000)")
time.sleep(5)

#TC6: Selecting the Profession and Tool

Profession_List = driver.find_elements(By.NAME, "profession")

print(len(Profession_List))

for Profession in Profession_List:
    Profession.click()

time.sleep(2)

Tool_List = driver.find_elements(By.NAME, "tool")

for Tools in Tool_List:
    Tools.click()

time.sleep(2)


#TC7: Selecting Options from the Defined CONTINENT Drop-down

driver.find_element(By.ID,"continents").click()

Select_Option = Select(driver.find_element(By.ID,"continents"))

Select_Option.select_by_visible_text("Africa")
time.sleep(3)
driver.find_element(By.ID,"continents").click()
time.sleep(2)

#TC8: Selecting Selenium Commands

Selenium_Options = Select(driver.find_element(By.ID, "selenium_commands"))

Selenium_Options.select_by_visible_text("Navigation Commands")
time.sleep(5)

#TC9: Uploading File

# driver.find_element(By.ID, "photo").send_keys("C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot 2024-07-05 175833.png")
# time.sleep(5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "photo")).click().perform()
time.sleep(3)
Key_Controller = Controller()
Key_Controller.type("C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot 2024-07-05 175833.png")
Key_Controller.press(Key.enter)
Key_Controller.release(Key.enter)
time.sleep(5)
