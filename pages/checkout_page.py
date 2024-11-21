from selenium.webdriver.support import expected_conditions as EC
from config.links import Links
from base.base_page import BasePage

class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    FIRST_NAME_FIELD = "xpath", "//input[@name='firstName']"
    LAST_NAME_FIELD = "xpath", "//input[@name='lastName']"
    POST_CODE_NAME_FIELD = "xpath", "//input[@id='postal-code']"
    BUTTON_CONTINUE = "xpath", "//input[@id='continue']"

    def input_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def input_last_name(self,last_name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(last_name)

    def input_post_code(self, post_code):
        self.wait.until(EC.element_to_be_clickable(self.POST_CODE_NAME_FIELD)).send_keys(post_code)

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CONTINUE)).click()