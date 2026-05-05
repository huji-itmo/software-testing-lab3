import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestThemeToggle:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_theme_toggle(self):
        self.driver.get("https://smi2.ru/")
        self.driver.set_window_size(1944, 1070)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        html_elem = self.driver.find_element(By.TAG_NAME, "html")
        initial_class = html_elem.get_attribute("class")

        theme_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[class*='ButtonTheme_btnTheme']")
            )
        )

        theme_btn.click()

        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        new_class = self.driver.find_element(By.TAG_NAME, "html").get_attribute("class")

        assert initial_class != new_class, "Theme toggle should change html class"

        print(f"Theme changed from {initial_class} to {new_class}")
