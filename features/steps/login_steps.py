from behave import given, when


@given('Open Reelly main page')
def open_reelly_main_page(context):
    context.driver.get("https://soft.reelly.io/sign-in")


@when('Log in to Reelly')
def log_in(context):
    context.app.login_page.login(
        "elaineoblitey@gmail.com",
        "Lane$unday23!!"
    )