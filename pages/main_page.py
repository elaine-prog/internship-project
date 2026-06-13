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
        time.sleep(5)
        self.js_click(self.MAIN_MENU)
        time.sleep(3)

        print("CURRENT URL AFTER MAIN MENU:", self.driver.current_url)
        print("PAGE TITLE:", self.driver.title)

    def click_connect_developer(self):
        print("CURRENT URL BEFORE CLICK:", self.driver.current_url)

        element = self.find_element(self.CONNECT_DEVELOPER_BTN)

        developer_url = element.get_attribute("href")

        self.driver.get(developer_url)

        print("URL AFTER OPENING DEVELOPER PAGE:", self.driver.current_url)

    def switch_to_new_tab(self):
        print("No new tab needed on BrowserStack.")

    def verify_connect_developer_page_opened(self):
        assert (
                "developer" in self.driver.current_url.lower()
                or "reelly.ai" in self.driver.current_url.lower()
        ), f"Wrong page opened: {self.driver.current_url}"