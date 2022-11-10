from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
from tests.conftest import driver


class HomePage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver                                            #initialization of driver happens here
    shop = (By.XPATH, "//a[contains(text(),'Shop')]")
    name = (By.CSS_SELECTOR,  "[name='name']")
    email = (By.CSS_SELECTOR,  "[name='email']")
    passwrd = (By.CSS_SELECTOR, "[type='Password']")
    check = (By.ID, "exampleCheck1")
    status = (By.ID, "inlineRadio2")
    gender = (By.ID, "exampleFormControlSelect1")
    dateofbirth = (By.XPATH, "/html/body/app-root/form-comp/div/form/div[7]/input")
    # dateofbirth = (By.XPATH, "//input[@type='date']")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div")

    # Initialization of driver and fetch "shop" element

    def shop_Items(self):
         return self.driver.find_element(*HomePage.shop)            #calling class and object created    # "*" -> to understand the shop created in HomePage as tuple
         # checkOutPage = CheckOutPage(self.driver)
         # return checkOutPage

        # self.driver.find_element(By.XPATH, value="//a[contains(text(),'Shop')]").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPasswrd(self):
        return self.driver.find_element(*HomePage.passwrd)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getEmpStatus(self):
        return self.driver.find_element(*HomePage.status)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getDateBirth(self):
        return self.driver.find_element(*HomePage.dateofbirth)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


