from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class CheckoutComplete(BasePage):

    PAGE_URL = Links.CHECKOUT_COMPLETE

    ORDER_FIELD = "xpath", "//h2[@class='complete-header']"
    BUTTON_BACK_HOME = "xpath", "//button[@id='back-to-products']"

    def check_your_order(self, order_text):
        order_element = self.wait.until(EC.visibility_of_element_located(self.ORDER_FIELD))
        order = order_element.text
        assert order == order_text, f"Значение текста {order}, а должно быть {order_text}"

    def click_back_home(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_BACK_HOME)).click()

    