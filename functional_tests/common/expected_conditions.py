from selenium.webdriver.support.expected_conditions import *


class text_to_be_present_in_element(object):
    def __init__(self, locator, text_, exact_match=False, ignore_case=False):
        self.locator = locator
        self.text = text_
        self.exact_match = exact_match
        self.ignore_case = ignore_case

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
        except StaleElementReferenceException:
            return False

        if self.exact_match:
            return element_text == self.text

        if self.ignore_case:
            self.text = self.text.lower()
            element_text = element_text.lower()
        return self.text in element_text


class absence_of_text_in_element_located(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
        except StaleElementReferenceException:
            return False
        return len(element_text) == 0


class elements_have_exact_count(object):
    def __init__(self, locator, expected_length):
        self.locator = locator
        self.expected_length = expected_length

    def __call__(self, driver):
        return len(_find_elements(driver, self.locator)) == self.expected_length


class url_is_updated(object):
    def __init__(self, current_url):
        self.current_url = current_url

    def __call__(self, driver):
        return driver.current_url != self.current_url


def _find_element(driver, by):
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e
