from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import OrderPage
from .pages.login_page import LoginPage
import pytest
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_order_book(browser, link):
#     page = OrderPage(browser, link)   
#     page.open()                      
#     page.go_to_order_page() 
#     page.go_to_alert_popup()
#     page.go_to_confirmation_info()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = OrderPage(browser, link)   
#     page.open()                      
#     page.go_to_order_page() 
#     #page.go_to_alert_popup()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = OrderPage(browser, link)   
#     page.open()                      
#     page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = OrderPage(browser, link)   
#     page.open()                      
#     page.go_to_order_page() 
#     page.should_not_be_disappeared()
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser = webdriver.Chrome()
        page = OrderPage(browser, link)
        page.open()
        page.go_to_login_page()
        page2 = LoginPage(browser, link)
        mail = "jsjs@fakemail.org"
        pass1 = "password1234" 
        page2.register_new_user()
        time.sleep(3)

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser = webdriver.Chrome()
        page = OrderPage(browser, link)
        page.open()                      
        page.should_not_be_success_message()

    def test_user_cant_see_product_in_basket_opened_from_product_pag(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser = webdriver.Chrome()
        page = BasePage(browser, link)
        page.open()
        page.test_guest_can_add_product_to_basket()

    # def test_user_should_see_login_link_on_product_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #     page = OrderPage(browser, link)
    #     page.open()
    #     page.should_be_login_link()

    # def test_user_can_go_to_login_page_from_product_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #     page = OrderPage(browser, link)
    #     page.open()
    #     page.go_to_login_page()
        
