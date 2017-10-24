from selenium import webdriver
import os


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome

    if context.config.userdata['BROWSER'] is None:
        BROWSER = 'firefox'
    else:
        BROWSER = context.config.userdata['BROWSER']

    if BROWSER == 'chrome':
        context.browser = webdriver.Remote(
                            command_executor='http://localhost:4444/wd/hub',
                            desired_capabilities={'browserName': 'chrome'})
    elif BROWSER == 'firefox':
        context.browser = webdriver.Remote(
                            command_executor='http://localhost:4444/wd/hub',
                            desired_capabilities={'browserName': 'firefox'})
    elif BROWSER == 'safari':
        context.browser = webdriver.Remote(
                            command_executor='http://localhost:4444/wd/hub',
                            desired_capabilities={'browserName': 'safari'})
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()
