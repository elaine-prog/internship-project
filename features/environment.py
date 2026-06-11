from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context):
    service = Service(
        GeckoDriverManager().install()
    )

    options = webdriver.FirefoxOptions()

    # Headless mode
    # options.add_argument("--headless")

    context.driver = webdriver.Firefox(
        service=service,
        options=options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)

    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'svetlanalevinsoh_pq9NLc'
    # bs_key = 'gg5H5exN3FjpwfZzXwpT'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.quit()
