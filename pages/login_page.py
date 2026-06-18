import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def login(self, email, password):
        self.input_text(email, self.EMAIL_FIELD)
        self.input_text(password, self.PASSWORD_FIELD)
        self.js_click(self.CONTINUE_BTN)
        time.sleep(5)

    def verify_user_logged_in(self):
        assert "find.reelly.io" in self.driver.current_url, \
            f"User is not logged in. Current URL: {self.driver.current_url}"