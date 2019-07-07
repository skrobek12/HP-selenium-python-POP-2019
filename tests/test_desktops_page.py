"""
Test methods for DesktopsPage.
"""

from pages.desktops_page import DesktopsPage
from tests.desktops_page_test_template import TestTemplate


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



