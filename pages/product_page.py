from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .login_page import LoginPage
from .locators import ProductPageLocators
import time

class OrderPage(BasePage): 
	def go_to_order_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
		login_link.click()
		time.sleep(2)

	def go_to_alert_popup(self):
		self.solve_quiz_and_get_code()

	def go_to_confirmation_info(self):
		confirm_info = self.browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
		confirm_info_text = confirm_info.text
		assert "Coders at Work" == confirm_info_text, "No such info"

	def should_not_be_success_message(self):
		assert self.is_not_element_present("#messages > div:nth-child(1) > div > strong"), "Success message is presented, but should not be"

	def should_not_be_disappeared(self):
		assert self.is_disappeared("#messages > div:nth-child(1) > div > strong"), "Success message is dissappear, but should not be"


