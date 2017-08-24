import unittest

from selenium import webdriver

from config.config import BS_COMMAND_EXECUTOR
from functional_tests.common.driver_api import DriverApi


class FunctionalTest(unittest.TestCase):
    command_executor = BS_COMMAND_EXECUTOR
    desired_capabilities = desired_cap = {'browser': 'Chrome',
                                          'browser_version': '55.0',
                                          'os': 'Windows',
                                          'os_version': '10',
                                          'resolution': '1024x768'}
    home_url = ''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(
            command_executor=cls.command_executor,
            desired_capabilities=cls.desired_capabilities)
        cls.driver_api = DriverApi(cls.driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == "__main__":
        import pdb; pdb.set_trace()
        # unittest.main()
