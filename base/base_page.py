from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10, poll_frequency=1)


    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_open(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))



