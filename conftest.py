from selenium import webdriver
import pytest
import time
import unittest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ar":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ar/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "ca":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ca/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "cs":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/cs/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "da":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/da/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "de":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "en":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "el":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/el/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "es":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "fi":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/fi/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "fr":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "it":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/it/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "ko":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ko/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "nl":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/nl/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "pl":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/pl/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "pt":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/pt/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "pt-br":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/pt-br/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "ro":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ro/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "ru":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "sk":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/sk/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "uk":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "zh-hans":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/zh-hans/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

