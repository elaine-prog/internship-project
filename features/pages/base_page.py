from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def input_text(self, text, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def js_click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )