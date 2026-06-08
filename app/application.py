from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)