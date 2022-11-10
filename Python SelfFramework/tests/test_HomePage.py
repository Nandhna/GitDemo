import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from python_utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        #driver.find_element(By.CSS_SELECTOR, value="[name='name']").send_keys("Rahul Shetty")
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])

        #driver.find_element(By.CSS_SELECTOR, value="[name='email']").send_keys("rahulshettyudemy@gmail.com")
        homepage = HomePage(self.driver)
        homepage.getEmail().send_keys(getData["emailid"])

#driver.find_element(By.CSS_SELECTOR, value="[type='Password']").send_keys("Rahulshetty@123")
        homepage = HomePage(self.driver)
        homepage.getPasswrd().send_keys(getData["password"])

#driver.find_element(By.ID, value="exampleCheck1").click()
        homepage = HomePage(self.driver)
        homepage.getCheckBox().click()

#sel = Select(driver.find_element(By.ID, value="exampleFormControlSelect1"))
#sel.select_by_visible_text("Male")

        self.selectOptionByText(homepage.getGender(), getData["gender"])

#driver.find_element(By.ID,value="inlineRadio2").click()
        homepage = HomePage(self.driver)
        homepage.getEmpStatus().click()

#driver.implicitly_wait(10)
#driver.find_element(By.CSS_SELECTOR, value="/html/body/app-root/form-comp/div/form/div[7]/label").send_keys("01/11/2022)
        homepage = HomePage(self.driver)
        Date = homepage.getDateBirth()
        time.sleep(2)
        Date.send_keys("01/11/2022")

#driver.find_element(By.XPATH("//input[@value='Submit']")).click()
        homepage = HomePage(self.driver)
        homepage.submitForm().click()

#alertText = driver.find_element(By.CSS_SELECTOR,value="[class* = 'alert-success']").text
        homepage = HomePage(self.driver)
        alertText= homepage.getSuccessMessage().text
        time.sleep(5)

        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param








