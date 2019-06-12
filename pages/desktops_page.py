"""
All methods and locators which will use to build tests for DesktopsPage.
"""

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DesktopsPage(BasePage):

    # Locators test_page__is_scrollable
    _privacy_footer = "//*[@id='footer']/div[2]/div[2]/ul/li[6]/a"
    # Locators test_logo_enabled
    _logo = "//*[@id='header']/div[2]/div[1]/div[1]/a"
    # Locators test_switch_to_youtube
    _youtube_button = "//*[@id='footer']/div[2]/div[1]/div[5]/ul/li[2]/ul/li[4]"
    _youtube_logo = "/html//div[@id='logo-icon-container']"
    # Locators test_switch_to_lindedin
    _linkedin_button = "//*[@id='footer']/div[2]/div[1]/div[5]/ul/li[2]/ul/li[2]"
    _linkedin_logo = "/html/body/header/div/a/li-icon"


    def check_title(self):
        return self._driver.title

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._privacy_footer).is_enabled()

    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def click_youtube_button(self):
        return self._driver.find_element_by_xpath(self._youtube_button).click()

    def is_youtube_button_enabled(self):
        return self._driver.find_element_by_xpath(self._youtube_logo).is_enabled()

    def click_linkedin_button(self):
        return self._driver.find_element_by_xpath(self._linkedin_button).click()

    def is_linkedin_button_enabled(self):
        return self._driver.find_element_by_xpath(self._linkedin_logo).is_enabled()





