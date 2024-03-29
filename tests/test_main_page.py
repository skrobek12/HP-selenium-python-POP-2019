"""
Test methods for MainPage.
"""

from pages.main_page import MainPage
from tests.main_page_test_template import TestTemplate
from time import sleep

class TestMainPage(TestTemplate):

    def test_logo_available(self):
        """
        Test is checking if logo is displayed at the main site..
        :return: True
        """
        m = MainPage(self.driver)
        assert m.is_logo_enabled() == True

    def test_page_is_scrollable(self):
        """
        Test is checking that page is scrollable.
        :return: True
        """
        m = MainPage(self.driver)
        m.scroll_down()
        assert m.is_footer_enabled() == True

    def test_open_search_button(self):
        """
        Test will be checking that open search button is enabled on the site.
        :return: True
        """
        m = MainPage(self.driver)
        assert m.is_button_open_search_enabled() == True

    def test_search_engine(self):
        """
        After clicking on the button open search, we will be input "test" word into search engine to checking that
        search engine is working correctly. Finally we should be on the search results card.
        :return: "Search Results for Test | Search HP"
        """
        m = MainPage(self.driver)
        m.click_button_open_search()
        sleep(1)
        m.click_engine_placeholder()
        m.clear_engine_placeholder()
        m.send_text_to_engine_placeholder()
        m.click_submit_search_button()
        assert m.is_link_testingHP_enabled() == True

    def test_desktops_menu(self):
        """
        After mouse hovering desktops button menu should be visible.
        :return: True
        """
        m = MainPage(self.driver)
        m.find_desktops_menu()
        m.mouse_hover_desktops_menu()
        assert m.is_desktops_menu_list_enabled() == True

    def test_printers_menu(self):
        """
        After mouse hovering printers button menu should be visible.
        :return: True
        """
        m = MainPage(self.driver)
        m.find_printers_menu()
        m.mouse_hover_printers_menu()
        assert m.is_printers_menu_list_enabled() == True

    def test_business_solutions_menu(self):
        """
        After mouse hovering business solutions button menu should be visible.
        :return: True
        """
        m = MainPage(self.driver)
        m.find_business_solutions_menu()
        m.mouse_hover_business_solutions_menu()
        assert m.is_business_solutions_menu_list_enabled() == True

    def test_support_menu(self):
        """
        After mouse hovering support button menu should be visible.
        :return: True
        """
        m = MainPage(self.driver)
        m.find_support_menu()
        m.mouse_hover_support_menu()
        assert m.is_support_menu_list_enabled() == True

    def test_filter_offered_products(self):
        """
        Test will be checking filter offered products
        :return: True
        """
        c = MainPage(self.driver)
        sleep(3)
        c.find_desktop_menu()
        sleep(3)
        c.mouse_hover_desktop_menu()
        sleep(3)
        c.click_towers_button()
        sleep(3)
        c.click_sale()
        sleep(3)
        c.click_ready_to_ship()
        sleep(3)
        c.click_home()
        sleep(3)
        assert c.is_hp_envy_button_enabled() == True


