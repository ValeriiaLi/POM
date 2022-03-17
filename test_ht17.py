from selenium import webdriver
import pytest
import time
import unittest


def test_store_button(browser):
     time.sleep(10)
     button = browser.find_element_by_css_selector("button.btn")
     print("\nButton exist")

