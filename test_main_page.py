from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   
#     page.open()                      
#     page.go_to_login_page() 
#     link2 = str(browser.current_url)
#     page2 = LoginPage(browser, link2)   
#     page2.open()                     
#     page2.should_be_login_page()        

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_product_pag(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(browser, link)
        page.open()
        page.should_go_to_box()
        

