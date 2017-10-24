from selenium.webdriver.common.by import By


class Locators(object):
    """A class for main page locators. All main page locators should come here"""
    DAY_1 = (By.XPATH, "//*[contains(@data-test,'day-1')]")
    DAY_2 = (By.XPATH, "//*[contains(@data-test,'day-2')]")
    DAY_5 = (By.XPATH, "//*[contains(@data-test,'day-5')]")
    DAY_2_HOUR_1 = (By.XPATH, "//*[contains(@data-test,'hour-2-1')]")
    DAY_2_HOUR_2 = (By.XPATH, "//*[contains(@data-test,'hour-2-2')]")
    DAY_2_HOUR_3 = (By.XPATH, "//*[contains(@data-test,'hour-2-3')]")

    HOURS = (By.CSS_SELECTOR, '.hour')
    CELL_ROWS = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/span[1]")

    CURRENT_CONDITION_2_1 = (By.XPATH, "//*[contains(@data-test,'description-2-1')]")
    MAX_TEMP_2_1 = (By.XPATH, "//*[contains(@data-test,'maximum-2-1')]")
    MIN_TEMP_2_1 = (By.XPATH, "//*[contains(@data-test,'minimum-2-1')]")
    WIND_SPEED_2_1 = (By.XPATH, "//*[contains(@data-test,'speed-2-1')]")
    WIND_DIRECTION_2_1 = (By.XPATH, "//*[contains(@data-test,'direction-2-1')]")
    AGGREGATE_RAINFALL_2_1 = (By.XPATH, "//*[contains(@data-test,'rainfall-2-1')]")

    CURRENT_CONDITION_2_2 = (By.XPATH, "//*[contains(@data-test,'description-2-2')]")
    MAX_TEMP_2_2 = (By.XPATH, "//*[contains(@data-test,'maximum-2-2')]")
    MIN_TEMP_2_2 = (By.XPATH, "//*[contains(@data-test,'minimum-2-2')]")
    WIND_SPEED_2_2 = (By.XPATH, "//*[contains(@data-test,'speed-2-2')]")
    WIND_DIRECTION_2_2 = (By.XPATH, "//*[contains(@data-test,'direction-2-2')]")
    AGGREGATE_RAINFALL_2_2 = (By.XPATH, "//*[contains(@data-test,'rainfall-2-2')]")

    CURRENT_CONDITION_2_3 = (By.XPATH, "//*[contains(@data-test,'description-2-3')]")
    MAX_TEMP_2_3 = (By.XPATH, "//*[contains(@data-test,'maximum-2-3')]")
    MIN_TEMP_2_3 = (By.XPATH, "//*[contains(@data-test,'minimum-2-3')]")
    WIND_SPEED_2_3 = (By.XPATH, "//*[contains(@data-test,'speed-2-3')]")
    WIND_DIRECTION_2_3 = (By.XPATH, "//*[contains(@data-test,'direction-2-3')]")
    AGGREGATE_RAINFALL_2_3 = (By.XPATH, "//*[contains(@data-test,'rainfall-2-3')]")

    CURRENT_CONDITION_1 = (By.XPATH, "//*[contains(@data-test,'description-1')]")
    MAX_TEMP_1 = (By.XPATH, "//*[contains(@data-test,'maximum-1')]")
    MIN_TEMP_1 = (By.XPATH, "//*[contains(@data-test,'minimum-1')]")
    WIND_SPEED_1 = (By.XPATH, "//*[contains(@data-test,'speed-1')]")
    WIND_DIRECTION_1 = (By.XPATH, "//*[contains(@data-test,'direction-1')]")
    AGGREGATE_RAINFALL_1 = (By.XPATH, "//*[contains(@data-test,'rainfall-1')]")

