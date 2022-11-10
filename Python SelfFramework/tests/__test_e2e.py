#from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.by import By


from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from python_utilities.BaseClass import BaseClass




class Test_one(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage= homePage.shop_Items()
        cards=checkoutPage.getCardTitles()


        #self.driver.find_element(By.XPATH, value="//a[contains(text(),'Shop')]").click()

        #cards = self.driver.find_elements(By.CSS_SELECTOR, value=".card-title a")

        i = -1
        for card in cards:
            i=i+1
            # i=0
            cardText = card.text
            print(cardText)
            if cardText == "iphone X":
                #self.driver.find_element(By.XPATH, value="//div[@class='card h-100']//descendant::button").click()
                #self.driver.find_element(By.CSS_SELECTOR, value="(.card-footer button)")
                checkoutPage.getCardFooter()[i].click()

        # self.driver.find_element(By.XPATH, value="(//button[text()='Add '])[4]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, value="//*[@id='navbarResponsive']/ul/li/a").click()
        time.sleep(2)

       # self.driver.find_element(By.XPATH, value="//tbody/tr[3]/td[5]/button[1]").click()
        confirmpage = checkoutPage.checkOutItems().click()


        self.driver.find_element(By.ID, value="country").send_keys("Ind")
        time.sleep(2)
        self.verifyLinkPresence("India")


        self.driver.find_element(By.LINK_TEXT, value="India").click()
        checkoutPage.checkValueCountry().click()


# checkbox
        #self.driver.find_element(By.XPATH, value="//div[@class='checkbox checkbox-primary']").click()
        checkoutPage.checkBoxItems().click()
        time.sleep(2)


# submit button
        #self.driver.find_element(By.CSS_SELECTOR, value="[type='submit']").click()
        checkoutPage.submitBoxButton().click()
        time.sleep(2)

