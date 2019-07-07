"""
All methods and locators which will use to build tests for DesktopsPage.
"""

from pages.base_page import BasePage


class DesktopsPage(BasePage):

    # Locators test_page__is_scrollable
    _privacy_footer = "//*[@id='footer']/div[2]/div[2]/ul/li[6]/a"
    # Locators test_logo_enabled
    _logo = "//*[@id='header']/div[2]/div[1]/div[1]/a"


    def check_title(self):
        return self._driver.title

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._privacy_footer).is_enabled()










