from selenium.webdriver.common.by import By


class Locators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    CITY_SEARCH_AREA = (By.ID, 'city')


