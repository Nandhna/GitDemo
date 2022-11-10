import time
from selenium import webdriver
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    # global driver

    browser_name=request.config.getoption("browser_name")
    print(browser_name)
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\NandhanaRajendran\\chromedriver_win32\\chromedriver.exe")
    # Firefox invocation Gecko Driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\NandhanaRajendran\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    elif browser_name == "edge":
         driver = webdriver.Edge(executable_path="C:\\Users\\NandhanaRajendran\\edgedriver_win32\\msedgedriver.exe")

    time.sleep(6)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

