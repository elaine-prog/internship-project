import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):

    MENU_BTN = (
        By.XPATH,
        "//div[contains(@class, 'menu-text') and contains(text(), 'Menu')]"
    )

    CONNECT_DEVELOPER_BTN = (
        By.CSS_SELECTOR,
        "a[href*='brm-for-developer']"
    )

    def open_main_menu_page(self):
        self.driver.get("https://soft.reelly.io/main-menu")

        print("CURRENT URL AFTER MAIN MENU:", self.driver.current_url)
        print("PAGE TITLE:", self.driver.title)

    def verify_main_menu_page_opened(self):
        assert (
            "menu" in self.driver.current_url.lower()
            or "main-menu" in self.driver.current_url.lower()
        ), f"Wrong page opened: {self.driver.current_url}"