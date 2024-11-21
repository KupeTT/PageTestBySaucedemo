import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
from pages.checkout_two import CheckoutTwo
from pages.card_page import CardPage
from pages.checkout_complete_page import CheckoutComplete

from config.data import Data

class BaseTest:

    data: Data

    login_page = LoginPage
    home_page = HomePage
    checkout_page = CheckoutPage
    checkout_two = CheckoutTwo
    card_page = CardPage
    checkout_complete_page = CheckoutComplete

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.checkout_two = CheckoutTwo(driver)
        request.cls.card_page = CardPage(driver)
        request.cls.checkout_complete_page = CheckoutComplete(driver)
        request.cls.data = Data()


