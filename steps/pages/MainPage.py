from selenium.webdriver.common.keys import Keys

from steps.locators import HomePageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    url = "http://localhost:3000/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)


class HomePage(BasePage):

    def is_title_matches(self):
        """Verifies that the hardcoded text "5 Weather Forecast" appears in page title"""
        return "5 Weather Forecast" in self.driver.title

    def enter_search_field(self, text):
        """Enter city in the search text field"""
        search_area = self.driver.find_element(*HomePageLocators.Locators.CITY_SEARCH_AREA)
        search_area.clear()
        search_area.send_keys(text)
        search_area.send_keys(Keys.RETURN)

    def click_go_button(self):
        """Triggers the search"""
        go_button = self.driver.find_element(*HomePageLocators.Locators.GO_BUTTON)
        go_button.click()


