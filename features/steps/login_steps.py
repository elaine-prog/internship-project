from behave import given, when, then


@given('Open Reelly main page')
def open_reelly_main_page(context):
    context.driver.get("https://soft.reelly.io/sign-in")


@when('Log in to Reelly')
def log_in(context):
    context.app.login_page.login(
        "elaineoblitey@gmail.com",
        "Lane$unday23!!"
    )


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.login_page.verify_user_logged_in()