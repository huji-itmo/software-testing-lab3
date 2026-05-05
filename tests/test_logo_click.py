import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogoClick:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_logo_click(self):
        self.driver.get("https://smi2.ru/publisher/2957")
        self.driver.set_window_size(1944, 1070)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        logo_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/']"))
        )

        logo_link.click()

        WebDriverWait(self.driver, 15).until(EC.url_to_be("https://smi2.ru/"))

        current_url = self.driver.current_url

        assert "smi2.ru" in current_url and current_url.endswith("smi2.ru/"), (
            "Should navigate to homepage"
        )

        print("Logo clicked, URL:", current_url)
