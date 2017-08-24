from selenium.common.exceptions import NoSuchElementException

from functional_tests.common.waits import DriverWaits


class DriverApi(object):

    def __init__(self, driver):
        self.driver = driver
        self.waits = DriverWaits(self.driver)

    def is_element_visible(self, css_selector):
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
        except NoSuchElementException:
            return False
        return element.is_displayed()
