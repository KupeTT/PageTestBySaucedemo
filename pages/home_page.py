import time

from config.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    BUTTON_ADD_T = "xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    BUTTON_ADD_JACK = "xpath", "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    BUTTON_ADD_BACKPACK = "xpath", "//button[@id='add-to-cart-sauce-labs-backpack']"
    BUTTON_SHOW_CARD = "xpath", "//a[@class='shopping_cart_link']"

    def click_t(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_T)).click()

    def click_jack(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_JACK)).click()

    def click_backpack(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_ADD_BACKPACK)).click()

    def click_card(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW_CARD)).click()



