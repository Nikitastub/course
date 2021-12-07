import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




# LANGUAGES = ['ru', 'en-gb', 'fr']

@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    def fin():
        browser.quit()
    request.addfinalizer(fin)
    return browser



def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--language", action="store", default="en-gb")