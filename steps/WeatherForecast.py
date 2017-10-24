from behave import *
from pages import MainPage
from pages import SearchResultsPage
from time import sleep

use_step_matcher("re")


@given("I am on the homepage")
def step_impl(context):
    driver = context.browser
    home_page = MainPage.HomePage(driver)
    home_page.navigate()
    assert home_page.is_title_matches(), "Error in loading homepage"


@when("I search for (?P<city>.+)")
def step_impl(context, city):
    driver = context.browser
    MainPage.HomePage(driver).enter_search_field(city)


@then("I get the weather forecast for the next 5 days")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_five_results_returned(), "5 results not returned as expected"


@then("I get an appropriate error message")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).no_results_found(), "check if test data folder updated with new cities"


@when("I click on the second day")
def step_impl(context):
    driver = context.browser
    SearchResultsPage.SearchPage(driver).click_on_second_result()


@then("I get atleast three hourly forecasts")
def step_impl(context):
    driver = context.browser
    three_hourly_forecasts = SearchResultsPage.SearchPage(driver).get_three_hourly_forecasts()
    print(three_hourly_forecasts)


@then("the hourly forecasts are hidden")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_hourly_results_returned(), "hourly forecasts not hidden"


@then("I check that current condition is displayed")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_current_condition_displayed(), "current condition not displayed"


@step("current wind speed with direction are displayed")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_wind_speed_displayed(), "wind speed is not displayed"
    assert SearchResultsPage.SearchPage(driver).is_wind_direction_displayed(), "wind direction is not displayed"


@step("aggregate rainfall is displayed and rounded off")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_aggregate_rainfall_displayed(), "aggregate rainfall is not displayed"
    """
    assumption here that the result is always an integer value
    """
    assert SearchResultsPage.SearchPage(driver).is_aggregate_rainfall_rounded_off(), "aggregate rainfall is not an integer value"


@step("minimum and maximum temperatures are displayed")
def step_impl(context):
    driver = context.browser
    assert SearchResultsPage.SearchPage(driver).is_min_temp_displayed(), "minimum temp not displayed"
    assert SearchResultsPage.SearchPage(driver).is_max_temp_displayed(), "max temperature not displayed"