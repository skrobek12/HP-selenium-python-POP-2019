"""
Test methods for StorePage.
"""

from pages.store_page import StorePage
from tests.store_page_test_template import TestTemplate
from time import sleep

class TestStorePage(TestTemplate):

    def test_logo_available(self):
        """
        Test is checking if logo is displayed at the desktops site.
        :return: True
        """
        c = StorePage(self.driver)
        assert c.is_logo_enabled() == True

    def test_page_is_scrollable(self):
        """
        Test is checking that page is scrollable.
        :return: True
        """
        c = StorePage(self.driver)
        c.scroll_down()
        assert c.is_footer_enabled() == True

    def test_change_language_website(self):
        """
        Test is checking that change language it works.
        :return: True
        """
        c = StorePage(self.driver)
        c.scroll_down()
        c.click_united_states_button()
        c.click_poland_button()
        assert c.is_securityPC_enabled() == True

    def test_sign_in(self):
        """
        Test is checking that sign in it works.
        :return: True
        """
        c = StorePage(self.driver)
        c.click_sign_in_and_register_button()
        c.click_sign_in()
        c.click_username()
        c.clear_username()
        c.send_text_to_username()
        c.click_confirm()
        c.click_password()
        c.clear_password()
        c.send_text_to_password()
        c.click_submit()
        c.click_welcome()
        assert c.is_account_enabled() == True





