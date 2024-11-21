from selenium.webdriver.support import expected_conditions as EC
from config.links import Links
from base.base_page import BasePage

class CardPage(BasePage):

    PAGE_URL = Links.CARD_PAGE

    BUTTON_CHECKOUT = "xpath", "//button[@id='checkout']"
    REMOVE_BUTTON = "xpath", ""
    JACK_DESCRIPTUON = "xpath", ""

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CHECKOUT)).click()