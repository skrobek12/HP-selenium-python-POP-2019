"""
Desktops Template is responsible for implementing WebDriver instance, get tested page, open window and maximize it.
"""

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://store.hp.com/us/en/cat/desktops")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()