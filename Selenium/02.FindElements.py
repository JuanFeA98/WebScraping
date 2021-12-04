import unittest
from pyunitreport import HTMLTestRunner 
from selenium import webdriver

class FindElements(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome(executable_path=r'C:/Users/jmart/Downloads/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        return super().setUp()

    def test_find_elements(self):
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')
        search_field = driver.find_element_by_id('search')
        button = driver.find_element_by_class_name('button')

    def tearDown(self):
        self.driver.quit()
        return super().tearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='FindElements'))