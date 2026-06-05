import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page import BasePage


class MainPage(BasePage):

    CONNECT_DEVELOPER_BTN = (
        By.XPATH,
        "//div[contains(text(),'Connect the developer')]"
    )

    def open_main_menu_page(self):
        self.driver.get("https://soft.reelly.io/main-menu")
        time.sleep(3)

    def click_connect_developer(self):
        self.scroll_to_element(self.CONNECT_DEVELOPER_BTN)
        time.sleep(1)
        self.js_click(self.CONNECT_DEVELOPER_BTN)

    def switch_to_new_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def verify_connect_developer_page_opened(self):
        assert (
            "developer" in self.driver.current_url.lower()
            or "reelly.ai" in self.driver.current_url.lower()
        ), f"Wrong page opened: {self.driver.current_url}"