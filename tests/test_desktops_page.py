"""
Test methods for DesktopsPage.
"""

from pages.desktops_page import DesktopsPage
from tests.desktops_page_test_template import TestTemplate
from time import sleep

class TestDesktopsPage(TestTemplate):

    def test_title(self):
        """
        Test is checking if title of page is correct.
        :return: "Desktop Computers"
        """
        c = DesktopsPage(self.driver)
        assert c.check_title() == "Desktop Computers"

    def test_page_is_scrollable(self):
        """
        Test is checking that page is scrollable.
        :return: True
        """
        c = DesktopsPage(self.driver)
        c.scroll_down()
        assert c.is_footer_enabled() == True

    def test_logo_available(self):
        """
        Test is checking if logo is displayed at the desktops site.
        :return: True
        """
        c = DesktopsPage(self.driver)
        assert c.is_logo_enabled() == True

    def test_switch_to_youtube(self):
        """
        Test will be checking switch to youtube site.
        :return: True
        """
        c = DesktopsPage(self.driver)
        c.scroll_down()
        c.click_youtube_button()
        sleep(10)
        assert c.is_youtube_button_enabled() == True

    def test_switch_to_linkedin(self):
        """
        Test will be checking switch to linkedin site.
        :return: True
        """
        c = DesktopsPage(self.driver)
        c.scroll_down()
        c.click_linkedin_button()
        assert c.is_linkedin_button_enabled() == True