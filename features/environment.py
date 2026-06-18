from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application

# BrowserStack imports (commented out for now)
# from selenium.webdriver.chrome.options import Options


def browser_init(context):

    # ===== LOCAL CHROME =====

    service = Service(
        ChromeDriverManager().install()
    )

    context.driver = webdriver.Chrome(
        service=service
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)

    # ===== BROWSERSTACK =====
    #
    # bs_user = 'YOUR_USERNAME'
    # bs_key = 'YOUR_ACCESS_KEY'
    #
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    #
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Tahoe",
    #     "browserName": "Safari",
    #     "sessionName": "Connect Developer Test",
    # }
    #
    # options.set_capability(
    #     "bstack:options",
    #     bstack_options
    # )
    #
    # context.driver = webdriver.Remote(
    #     command_executor=url,
    #     options=options
    # )
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    #
    # context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()