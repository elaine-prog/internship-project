from behave import when, then


@when('Open Main Menu page')
def open_main_menu_page(context):
    context.app.main_page.open_main_menu_page()


@when('Click on Connect the developer')
def click_connect_developer(context):
    context.app.main_page.click_connect_developer()


@when('Switch to the new tab')
def switch_to_new_tab(context):
    context.app.main_page.switch_to_new_tab()


@then('Verify the right Connect the developer tab opens')
def verify_right_connect_developer_tab_opens(context):
    context.app.main_page.verify_connect_developer_page_opened()