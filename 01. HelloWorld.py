import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    # @classmethod
    def setUp(sls):
        sls.driver =webdriver.Chrome(executable_path=r'C:/Users/jmart/Downloads/chromedriver.exe')
        driver = sls.driver
        driver.implicitly_wait(10)
        return super().setUp()

    def test_hello_world(self): 
        driver = self.driver
        driver.get('https://www.google.com')

    # @classmethod
    def tearDown(sls):
        sls.driver.quit()
        return super().tearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))