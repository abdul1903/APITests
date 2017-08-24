from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from config.config import DEFAULT_TIMEOUT
from functional_tests.common import expected_conditions as EC
from functional_tests.common.utils import get_css_selector_key


class DriverWaits(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_till_text_appeared(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'No text is attached in the element ({}) in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until_not(
            EC.absence_of_text_in_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_text_equals(self, css_selector, expected_text, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Text in the element({}) is not equal to \'{}\'. css selector: \'{}\''.format(
            css_selector_key, expected_text, css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), expected_text, exact_match=True),
            message=error_message)

    def wait_till_text_contains(self, css_selector, expected_text, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Text in the element ({}) does not contain \'{}\'. css selector: \'{}\''.format(
            css_selector_key, expected_text, css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), expected_text, ignore_case=True),
            message=error_message)

    def wait_till_length_equals(self, css_selector, expected_length, wait_time=DEFAULT_TIMEOUT,
                                message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Number of elements ({}) is not equal to {}. css selector: \'{}\''.format(
            css_selector_key, str(expected_length), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.elements_have_exact_count((By.CSS_SELECTOR, css_selector), expected_length), message=error_message)

    def wait_till_element_is_visible(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Element ({}) does not get visible in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_text_is_visible(self, tag, text, wait_time=DEFAULT_TIMEOUT, message=None):
        xpath_selector = "//%s[contains(.,'%s')]" % (tag, text)
        default_error_message = 'Element does not get visible in {} seconds. Text: \'{}\''.format(str(wait_time), text)
        error_message = message or default_error_message
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, xpath_selector)), message=error_message)

    def wait_till_element_is_found_by_xpath(self, xpath_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'Element does not get visible in {} seconds. xpath_selector: \'{}\''.format(
            str(wait_time), xpath_selector)
        error_message = message or default_error_message
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath_selector)), message=error_message)

    def wait_till_element_is_invisible(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Element ({}) does not get invisible in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_element_is_clickable(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Element ({}) does not get clickable in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_checkbox_is_clickable(self, text, wait_time=DEFAULT_TIMEOUT, message=None):
        xpath_selector = "//label[contains(.,'%s')]/../input[@type='checkbox']" % text
        default_error_message = 'Element does not get clickable in {} seconds. xpath selector: \'{}\''.format(
            str(wait_time), xpath_selector)

        error_message = message or default_error_message
        WebDriverWait(self.driver, wait_time).until(lambda s: s.find_element(By.XPATH, xpath_selector).is_enabled(),
                                                    message=error_message)

    def wait_till_element_is_present(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'Element ({}) is not attached in DOM in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_website_form_is_shown(self):
        self.wait_till_element_is_visible('.website-metadata-form')

    def wait_till_all_elements_visible(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        css_selector_key = get_css_selector_key(css_selector)
        default_error_message = 'No element ({}) get visible in {} seconds. css selector: \'{}\''.format(
            css_selector_key, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_url_is_updated(self, current_url, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'URL is not updated in {} seconds. current URL: \'{}\''.format(str(wait_time),
                                                                                               current_url)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.url_is_updated(current_url), message=error_message)
