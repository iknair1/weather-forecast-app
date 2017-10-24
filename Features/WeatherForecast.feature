Feature: 5 day weather forecast

  @local
  Scenario: Check for a valid city search 5 day results returned
     Given I am on the homepage
     When I search for edinburgh
     Then I get the weather forecast for the next 5 days

  @local
  Scenario: Check for a valid city search daily forecast is summarized
     Given I am on the homepage
     When I search for aberdeen
     Then I check that current condition is displayed
     And current wind speed with direction are displayed
     And aggregate rainfall is displayed and rounded off
     And minimum and maximum temperatures are displayed

  @local
  Scenario: Check that hourly forecasts can be expanded and collapsed
     Given I am on the homepage
     When I search for dundee
     And I click on the second day
     Then I get atleast three hourly forecasts
     When I click on the second day
     Then the hourly forecasts are hidden

  @local
  Scenario Outline: Check for invalid city appropriate error message seen
     Given I am on the homepage
     When I search for a given <city>
     Then I get an appropriate error message
   Examples:
   |city                |
   | london             |
   | @@!!!@@@12         |


