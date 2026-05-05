import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCardViewToggle:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_card_view_toggle(self):
        self.driver.get("https://smi2.ru/")
        self.driver.set_window_size(1944, 1070)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        card_view_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[class*='BtnCardLineViev_filterCard']")
            )
        )

        card_view_btn.click()

        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        print("View toggled to card view")
