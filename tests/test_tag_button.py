import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTagButton:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tag_button(self):
        self.driver.get("https://smi2.ru/")
        self.driver.set_window_size(1944, 1070)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        sport_tag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '/tematiks/16')]")
            )
        )

        sport_tag.click()

        WebDriverWait(self.driver, 15).until(EC.url_contains("tematiks/16"))

        current_url = self.driver.current_url

        assert "tematiks/16" in current_url, "Should navigate to sports topic"

        print("Sport tag clicked, URL:", current_url)
