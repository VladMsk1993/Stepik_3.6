from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def language():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)




def pytest_addoption(parser):
    parser.addoption('--language_name', action='store', default="En",
                     help="Choose language: en or fr")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language_name")
    browser = None
    if language_name == "en":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif language_name == "fr":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language_name should be en or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()