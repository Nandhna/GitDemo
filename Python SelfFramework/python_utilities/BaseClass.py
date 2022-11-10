import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)                                                       #filehandler exception

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self,text):
# Suggestions are taking time to load results in drop-down
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))                     #Can be used to Rerun "DATA" multiple times

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
