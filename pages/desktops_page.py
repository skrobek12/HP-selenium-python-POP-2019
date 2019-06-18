"""
All methods and locators which will use to build tests for DesktopsPage.
"""

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DesktopsPage(BasePage):

    # Locators test_page__is_scrollable
    _privacy_footer = "//*[@id='footer']/div[2]/div[2]/ul/li[6]/a"
    # Locators test_logo_enabled
    _logo = "//*[@id='header']/div[2]/div[1]/div[1]/a"
    # Locators test_switch_to_facebook
    _facebook_button = "//*[@id='footer']/div[2]/div[1]/div[5]/ul/li[2]/ul/li[1]"
    _facebook_logo = "//*[@id='blueBarDOMInspector']/div/div/div/div[1]/a/i"
    # Locators test_switch_to_twitter
    _twitter_button = "//*[@id='footer']/div[2]/div[1]/div[5]/ul/li[2]/ul/li[3]"
    _twitter_logo = "//*[@id='global-nav-home']/a"
    # Locators test_switch_to_youtube
    _youtube_button = "//*[@id='footer']/div[2]/div[1]/div[5]/ul/li[2]/ul/li[4]/a"
    _youtube_logo = "//*[@id='logo-icon-container']"


    def check_title(self):
        return self._driver.title

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._privacy_footer).is_enabled()

    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def click_facebook_button(self):
        return self._driver.find_element_by_xpath(self._facebook_button).click()

    def is_facebook_button_enabled(self):
        return self._driver.find_element_by_xpath(self._facebook_logo).is_enabled()

    def click_twitter_button(self):
        return self._driver.find_element_by_xpath(self._twitter_button).click()

    def is_twitter_button_enabled(self):
        return self._driver.find_element_by_xpath(self._twitter_logo).is_enabled()

    def click_youtube_button(self):
        return self._driver.find_element_by_xpath(self._youtube_button).click()

    def is_youtube_button_enabled(self):
        return self._driver.find_element_by_xpath(self._youtube_logo).is_enabled()








