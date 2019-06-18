"""
All methods and locators which will use to build tests for MainPage.
"""

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MainPage(BasePage):

    # Locators test_logo_enabled
    _logo = "/html//div[@id='header']//a[@name='1414644']"

    # Locators test_page_is_scrollable
    _original_footer = "//*[@id='footer']/div[2]/div[2]/ul/li[1]"

    # Locators test_button_open_search
    _open_search_button = "//*[@id='search_widget']"

    # Loacators test_search_engine:
    _search_engine_placeholder = "//*[@id='searchBox']"
    _submit_search_button = "//*[@id='searchHP']/div/div[1]/button"
    _search_value = "Test"
    _link_testingHP = "//*[@id='results']/div/div[3]/h3/a"
    # Text to send
    TEXT_SEND_SEARCH_ENGINE = "Test"

    # Locators test_desktops_menu
    _desktops_menu = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[2]"
    _desktops_menu_list = "//*[@id='header']/div[2]/div[1]/div[3]/ul[2]"

    # Locators test_printers_menu
    _printers_menu = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[3]"
    _printers_menu_list = "//*[@id='header']/div[2]/div[1]/div[3]/ul[3]"

    # Locators test_business_solutions_menu
    _business_solutions_menu = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[7]"
    _business_solutions_menu_list = "//*[@id='header']/div[2]/div[1]/div[3]/ul[4]"

    # Locators test_support_menu
    _support_menu = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[8]"
    _support_menu_list = "//*[@id='header']/div[2]/div[1]/div[3]/ul[5]"

    # Locators test_filter_offered_products
    _desktops = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[2]"
    _towers_button = "//*[@id='header']/div[2]/div[1]/div[2]/ul/li[2]/div[2]"
    _sale = "//*[@id='facetItem_xonsale']/label/span[1]"
    _ready_to_ship = "//*[@id='facetItem_ads_f30001_ntk_cs_0']/label/span[1]"
    _home = "//*[@id='facetItem_ads_f38501_ntk_cs_0']/label/span[1]"
    _hp_slimline = "//*[@id='p_3074457345618854362']"


    def is_logo_enabled(self):
        return self._driver.find_element_by_xpath(self._logo).is_enabled()

    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._original_footer).is_enabled()

    def is_button_open_search_enabled(self):
        return self._driver.find_element_by_xpath(self._open_search_button).is_enabled()

    def click_button_open_search(self):
        return self._driver.find_element_by_xpath(self._open_search_button).click()

    def click_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).click()

    def clear_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).clear

    def send_text_to_engine_placeholder(self):
        return self._driver.find_element_by_xpath(self._search_engine_placeholder).send_keys(self.TEXT_SEND_SEARCH_ENGINE)

    def click_submit_search_button(self):
        wait = WebDriverWait(self._driver,2)
        return wait.until(EC.element_to_be_clickable((By.XPATH,self._submit_search_button))).click()

    def is_link_testingHP_enabled(self):
        return self._driver.find_element_by_xpath(self._link_testingHP).is_enabled()

    def check_title(self):
        return self._driver.title

    def find_desktops_menu(self):
        return self._driver.find_element_by_xpath(self._desktops_menu)

    def mouse_hover_desktops_menu(self):
        actions = ActionChains(self._driver)
        return actions.move_to_element(self._driver.find_element_by_xpath(self._desktops_menu)).perform()

    def is_desktops_menu_list_enabled(self):
        return self._driver.find_element_by_xpath(self._desktops_menu_list).is_enabled()

    def find_printers_menu(self):
        return self._driver.find_element_by_xpath(self._printers_menu)

    def mouse_hover_printers_menu(self):
        actions = ActionChains(self._driver)
        return actions.move_to_element(self._driver.find_element_by_xpath(self._printers_menu)).perform()

    def is_printers_menu_list_enabled(self):
        return self._driver.find_element_by_xpath(self._printers_menu_list).is_enabled()

    def find_business_solutions_menu(self):
        return self._driver.find_element_by_xpath(self._business_solutions_menu)

    def mouse_hover_business_solutions_menu(self):
        actions = ActionChains(self._driver)
        return actions.move_to_element(self._driver.find_element_by_xpath(self._business_solutions_menu)).perform()

    def is_business_solutions_menu_list_enabled(self):
        return self._driver.find_element_by_xpath(self._business_solutions_menu_list).is_enabled()

    def find_support_menu(self):
        return self._driver.find_element_by_xpath(self._support_menu)

    def mouse_hover_support_menu(self):
        actions = ActionChains(self._driver)
        return actions.move_to_element(self._driver.find_element_by_xpath(self._support_menu)).perform()

    def is_support_menu_list_enabled(self):
        return self._driver.find_element_by_xpath(self._support_menu_list).is_enabled()

    def find_desktop_menu(self):
        return self._driver.find_element_by_xpath(self._desktops)

    def mouse_hover_desktop_menu(self):
        actions = ActionChains(self._driver)
        return actions.move_to_element(self._driver.find_element_by_xpath(self._desktops)).perform()

    def click_towers_button(self):
        return self._driver.find_element_by_xpath(self._towers_button).click()

    def click_sale(self):
        return self._driver.find_element_by_xpath(self._sale).click()

    def click_ready_to_ship(self):
        return self._driver.find_element_by_xpath(self._ready_to_ship).click()

    def click_home(self):
        return self._driver.find_element_by_xpath(self._home).click()

    def is_hp_slimeline_button_enabled(self):
        return self._driver.find_element_by_xpath(self._hp_slimline).is_enabled()

