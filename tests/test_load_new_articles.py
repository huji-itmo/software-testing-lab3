import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLoadNewArticles:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_load_new_articles(self):
        self.driver.get("https://smi2.ru/")
        self.driver.set_window_size(1944, 1070)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

        try:
            load_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button[class*='ArticlesFeed_applyNewArticlesBtn']",
                    )
                )
            )

            if load_btn:
                load_btn.click()

                WebDriverWait(self.driver, 5).until(
                    lambda d: (
                        d.execute_script("return document.readyState") == "complete"
                    )
                )

                print("Load new articles button clicked")
        except Exception as e:
            print("No new articles button found:", str(e))
