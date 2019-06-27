"""
All methods and locators which will use to build tests for StorePage.
"""

from pages.base_page import BasePage



class StorePage(BasePage):

    # Locators test_logo_enabled
    _logo = "//*[@id='header']/div[2]/div[1]/div[1]/a"

    # Locators test_page_is_scrollable
    _site_map = "//*[@id='footer']/div[2]/div[2]/ul/li[5]/a"
    # Locators test_change_language_website
    _united_states = "//*[@id='footer']/div[1]/div/div/div/a/span[4]"
    _poland = "//*[@id='footer']/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/ul/li[55]/a"
    _security_PC = "//*[@id='body']/div[3]/div[1]/div/div/div/div/a[2]/span"
    # Locators test_sign_in_on_account
    _sign_in_and_register = "//*[@id='utilityNav']/div/nav/section/ul/li[5]/a"
    _sign_in = "//*[@id='utilityNav']/div/nav/section/ul/li[5]/ul/li[1]/a"
    _username = "//*[@id='username']"
    _confirm = "//*[@id='next_button']"
    _password = "//*[@id='password']"
    _submit = "//*[@id='root']/div/div/div/div/div/div[2]/div/div/button"
    _welcome = "//*[@id='utilityNav']/div/nav/section/ul/li[5]/a"
    _my_account = "//*[@id='utilityNav']/div/nav/section/ul/li[5]/ul/li[2]/a"
    #Text to send
    TEXT_SEND_USERNAME = "tester12@gmail.com"
    TEXT_SEND_PASSWORD = "Skrobek12"



    def is_footer_enabled(self):
        return self._driver.find_element_by_xpath(self._site_map).is_enabled()

    def click_united_states_button(self):
        return self._driver.find_element_by_xpath(self._united_states).click()

    def click_poland_button(self):
        return self._driver.find_element_by_xpath(self._poland).click()

    def is_securityPC_enabled(self):
        return self._driver.find_element_by_xpath(self._security_PC).is_enabled()

    def click_sign_in_and_register_button(self):
        return self._driver.find_element_by_xpath(self._sign_in_and_register).click()

    def click_sign_in(self):
        return self._driver.find_element_by_xpath(self._sign_in).click()

    def click_username(self):
        return self._driver.find_element_by_xpath(self._username).click()

    def clear_username(self):
        return self._driver.find_element_by_xpath(self._username).clear

    def send_text_to_username(self):
        return self._driver.find_element_by_xpath(self._username).send_keys(self.TEXT_SEND_USERNAME)

    def click_confirm(self):
        return self._driver.find_element_by_xpath(self._confirm).click()

    def click_password(self):
        return self._driver.find_element_by_xpath(self._password).click()

    def clear_password(self):
        return self._driver.find_element_by_xpath(self._password).clear

    def send_text_to_password(self):
        return self._driver.find_element_by_xpath(self._password).send_keys(self.TEXT_SEND_PASSWORD)

    def click_submit(self):
        return self._driver.find_element_by_xpath(self._submit).click()

    def click_welcome(self):
        return self._driver.find_element_by_xpath(self._welcome).click()

    def is_account_enabled(self):
        return self._driver.find_element_by_xpath(self._my_account).is_enabled()




