import pytest
from selenium import webdriver
from conftest import *


@pytest.fixture(scope="function")
def aproving_button(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_id("id_quantity")
    button.click()
