import time

from base.base_test import BaseTest

class TestSite(BaseTest):

    def test_buy_clothes(self):
        self.login_page.open()
        self.login_page.is_open()
        self.login_page.input_login(self.data.LOGIN_STANDARD)
        self.login_page.input_password(self.data.PASSWORD_STANDARD)
        self.login_page.click_button_login()
        self.home_page.is_open()
        self.home_page.click_t()
        self.home_page.click_jack()
        self.home_page.click_backpack()
        self.home_page.click_card()
        self.card_page.is_open()
        self.card_page.click_checkout()
        self.checkout_page.is_open()
        self.checkout_page.input_first_name("Daw")
        self.checkout_page.input_last_name("Jaw")
        self.checkout_page.input_post_code("221020")
        self.checkout_page.click_button()
        self.checkout_two.is_open()
        self.checkout_two.check_ship_text("Free Pony Express Delivery!")
        self.checkout_two.check_tax_text("Tax: $7.68")
        self.checkout_two.check_total_price("Total: $103.65")
        self.checkout_two.click_button_finish()
        self.checkout_complete_page.is_open()
        self.checkout_complete_page.check_your_order("Thank you for your order!")
        self.checkout_complete_page.click_back_home()