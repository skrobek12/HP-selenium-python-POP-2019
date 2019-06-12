"""
BasePage class initialized driver.
"""

class BasePage(object):

    def __init__(self, driver):
        self._driver = driver

    def scroll_down(self):
        return self._driver.execute_script("window.scrollTo(0, 4000)")