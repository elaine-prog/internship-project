import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):

    MAIN_MENU = (
        By.XPATH,
        "//span[contains(text(), 'Main menu')]"
    )

    CONNECT_DEVELOPER_BTN = (
        By.CSS_SELECTOR,
        "a[href*='brm-for-developer']"
    )

    def open_main_menu_page(self):
        self.js_click(self.MAIN_MENU)
        time.sleep(2)

        print("CURRENT URL AFTER MAIN MENU:", self.driver.current_url)
        print("PAGE TITLE:", self.driver.title)

    def click_connect_developer(self):
        print("CURRENT URL BEFORE CLICK:", self.driver.current_url)

        self.scroll_to_element(self.CONNECT_DEVELOPER_BTN)
        time.sleep(1)
        self.js_click(self.CONNECT_DEVELOPER_BTN)

    def switch_to_new_tab(self):
        time.sleep(2)

        tabs = self.driver.window_handles

        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[-1])
        else:
            print("No new tab opened. Staying on current tab.")



    def verify_connect_developer_page_opened(self):
        assert (
            "developer" in self.driver.current_url.lower()
            or "reelly.ai" in self.driver.current_url.lower()
        ), f"Wrong page opened: {self.driver.current_url}"