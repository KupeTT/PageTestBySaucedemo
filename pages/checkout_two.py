from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTwo(BasePage):

    PAGE_URL = Links.CHECKOUT_TWO_PAGE

    SHIP_INFO = "xpath", "(//div[@class='summary_value_label'])[2]"
    TAX_INFO = "xpath", "//div[@class='summary_tax_label']"
    TOTAL_INFO = "xpath", "//div[@class='summary_total_label']"
    BUTTON_FINISH = "xpath", "//button[@id='finish']"

    def check_ship_text(self, shipping_info):
        ship_element = self.wait.until(EC.visibility_of_element_located(self.SHIP_INFO))
        ship = ship_element.text
        assert ship == shipping_info, f"Значение текста {ship}, а должно быть {shipping_info}"
        print(ship_element.text)


    def check_tax_text(self, tax_info):
    # def check_tax_text(self):
        tax_element = self.wait.until(EC.visibility_of_element_located(self.TAX_INFO))
        tax = tax_element.text
        assert tax == tax_info, f"Значение текста {tax}, а должно быть {tax_info}"
        print(tax_element.text)

    def check_total_price(self, price_info):
    # def check_total_price(self):
        total_price_element = self.wait.until(EC.visibility_of_element_located(self.TOTAL_INFO))
        total_price = total_price_element.text
        assert total_price == price_info, f"Значение текста {total_price}, а должно быть {price_info}"
        print(total_price_element.text)


    def click_button_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_FINISH)).click()

