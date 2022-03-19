from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pytest
import unittest
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def register_new_user(self):
        email = self.browser.find_element_by_css_selector("#id_registration-email")
        email_data = str(time.time()) + "@fakemail.org"
        email.send_keys(email_data)
        password1 = self.browser.find_element_by_css_selector("#id_registration-password1")
        password1.send_keys("Valeriia22")
        password2 = self.browser.find_element_by_css_selector("#id_registration-password2")
        password2.send_keys("Valeriia22")
        button = self.browser.find_element_by_css_selector("#register_form > button")
        button.click()
        
