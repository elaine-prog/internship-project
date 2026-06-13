from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app.application import Application


def browser_init(context, scenario_name):

    bs_user = 'elaineoblitey_GqhT0b'
    bs_key = 'mPoZG7heZ47ii87ukpPg'

    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()

    bstack_options = {
        "os": "OS X",
        "osVersion": "Tahoe",
        "browserName": "Safari",
        "sessionName": scenario_name,
    }

    options.set_capability(
        "bstack:options",
        bstack_options
    )

    context.driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()