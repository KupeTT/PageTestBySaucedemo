from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USER_FIELD = "xpath", "//input[@placeholder='Username']"
    PASSWORD_FIELD = "xpath", "//input[@placeholder='Password']"
    LOGIN_BUTTON = "xpath", "//input[@name='login-button']"

    def input_login(self,login):
        self.wait.until(EC.visibility_of_element_located(self.USER_FIELD)).send_keys(login)

    def input_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_button_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

