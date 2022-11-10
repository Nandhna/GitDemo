from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver


    cardTitle = (By.CSS_SELECTOR,".card-title a")


    #instead of cards = self.driver.find_elements(By.CSS_SELECTOR, value=".card-title a")
    cardFooter = (By.XPATH, "//div[@class='card h-100']//descendant::button")

    #instead of  self.driver.find_element(By.XPATH, value="//tbody/tr[3]/td[5]/button[1]").click()
    checkOut = (By.XPATH,"//tbody/tr[4]/td[5]/button[1]")

    # self.driver.find_element(By.LINK_TEXT, value="India").click()
    checkValueCountry = (By.LINK_TEXT,"India")

    # self.driver.find_element(By.XPATH, value="//div[@class='checkbox checkbox-primary']").click()
    checkBoxItems = (By.XPATH,"//div[@class='checkbox checkbox-primary']")

    # self.driver.find_element(By.CSS_SELECTOR, value="[type='submit']").click()
    submitBoxButton = (By.CSS_SELECTOR,"[type='submit']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)
        # confirmPage = ConfirmPage(self.driver)
        # return confirmPage

    def checkValueCountryElt(self):
        return self.driver.find_element(*CheckOutPage.checkValueCountry)

    def checkBoxItemsElt(self):
        return self.driver.find_element(*CheckOutPage.checkBoxItems)

    def submitBoxButtonElt(self):
        return self.driver.find_element(*CheckOutPage.submitBoxButton)






