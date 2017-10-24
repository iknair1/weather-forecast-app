from time import sleep
from locators import SearchPageLocators
from pages import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(MainPage.HomePage):
    """Search results page action methods come here"""

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, ".hour")))

    def no_results_found(self):
        return "Error retrieving the forecast" in self.driver.page_source

    def is_five_results_returned(self):
        """
        check if 5 results returned
        """
        day_5 = self.driver.find_element(*SearchPageLocators.Locators.DAY_5)
        if day_5.is_displayed():
            return True
        else:
            return False

    def click_on_second_result(self):
        self.driver.find_element(*SearchPageLocators.Locators.DAY_2).click()

    def get_three_hourly_forecasts(self):
        day1_forecast = [self.driver.find_element(*SearchPageLocators.Locators.DAY_2_HOUR_1).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MIN_TEMP_2_1).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MAX_TEMP_2_1).text,
                 self.driver.find_element(*SearchPageLocators.Locators.WIND_SPEED_2_1).text,
                 self.driver.find_element(*SearchPageLocators.Locators.AGGREGATE_RAINFALL_2_1).text
                 ]
        day2_forecast = [self.driver.find_element(*SearchPageLocators.Locators.DAY_2_HOUR_2).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MIN_TEMP_2_2).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MAX_TEMP_2_2).text,
                 self.driver.find_element(*SearchPageLocators.Locators.WIND_SPEED_2_2).text,
                 self.driver.find_element(*SearchPageLocators.Locators.AGGREGATE_RAINFALL_2_2).text
                 ]
        day3_forecast = [self.driver.find_element(*SearchPageLocators.Locators.DAY_2_HOUR_3).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MIN_TEMP_2_3).text,
                 self.driver.find_element(*SearchPageLocators.Locators.MAX_TEMP_2_3).text,
                 self.driver.find_element(*SearchPageLocators.Locators.WIND_SPEED_2_3).text,
                 self.driver.find_element(*SearchPageLocators.Locators.AGGREGATE_RAINFALL_2_3).text
                 ]
        return day1_forecast + day2_forecast + day3_forecast

    def is_hourly_results_returned(self):
        sleep(2)
        hour_row = self.driver.find_element(*SearchPageLocators.Locators.CELL_ROWS)
        if hour_row.is_displayed():
            return False
        else:
            return True

    def is_current_condition_displayed(self):
        current_condition = self.driver.find_element(*SearchPageLocators.Locators.CURRENT_CONDITION_1)
        if current_condition.is_displayed():
            return True
        else:
            return False

    def is_wind_speed_displayed(self):
        wind_speed = self.driver.find_element(*SearchPageLocators.Locators.WIND_SPEED_1)
        if wind_speed.is_displayed():
            return True
        else:
            return False

    def is_wind_direction_displayed(self):
        wind_direction = self.driver.find_element(*SearchPageLocators.Locators.WIND_DIRECTION_1)
        if wind_direction.is_displayed():
            return True
        else:
            return False

    def is_max_temp_displayed(self):
        max_temp = self.driver.find_element(*SearchPageLocators.Locators.MAX_TEMP_1)
        if max_temp.is_displayed():
            return True
        else:
            return False

    def is_min_temp_displayed(self):
        min_temp = self.driver.find_element(*SearchPageLocators.Locators.MIN_TEMP_1)
        if min_temp.is_displayed():
            return True
        else:
            return False

    def is_aggregate_rainfall_displayed(self):
        agg_rainfall = self.driver.find_element(*SearchPageLocators.Locators.AGGREGATE_RAINFALL_1)
        if agg_rainfall.is_displayed():
            return True
        else:
            return False

    def is_aggregate_rainfall_rounded_off(self):
        agg_rainfall = self.driver.find_element(*SearchPageLocators.Locators.AGGREGATE_RAINFALL_1)
        return type(agg_rainfall.text)
