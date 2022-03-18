from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #elements = self.find_elements_by_partial_link_text('login')
        #assert elements in self.url, "Login link is not presented"
        time.sleep(5)
        assert "login" in str(self.browser.current_url), "login is absent in current url"
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_EMAIL), "Email is not presented"
        assert self.is_element_present(*LoginPageLocators.AUTH_PASSWORD), "Password is not presented"
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD2), "Password confirmation is not presented"
        #assert True