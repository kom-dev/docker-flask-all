import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class FlaskServerTestCase(unittest.TestCase):

    def setUp(self):
        ## create an object BROWSER in this unittest class in order to execute selenium actions,
        ## here selenium host is based on the docker links in docker-compose.yml
        self.BROWSER = webdriver.Remote(command_executor='http://selenium:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
        self.BROWSER.implicitly_wait(5)
        ## here flask_server host is based on the docker links in docker-compose.yml
        self.BROWSER.get('http://flask_server:5000')

    def tearDown(self):
        self.BROWSER.quit()

    def test_Home_Page(self):
        self.assertIn('Web Server Devops Formation', self.BROWSER.title)
        ## Save home page as an image
        self.BROWSER.get_screenshot_as_file('/results/home_screenshot.png')

    def BaseTestSimpleDivision(self, v1, v2, expectedResult):
        val1 = self.BROWSER.find_element_by_id('valeur1')
        val1.clear()
        val1.send_keys(v1)
        val1.send_keys(Keys.RETURN)
        time.sleep(1)
        val2 = self.BROWSER.find_element_by_id('valeur2')
        val2.clear()
        val2.send_keys(v2)
        val2.send_keys(Keys.RETURN)
        time.sleep(1)
        ValiderBtn = self.BROWSER.find_element_by_id('submit')
        ValiderBtn.click()
        time.sleep(1)
        ph = self.BROWSER.find_element_by_class_name('page-header')
        self.assertIn(": " + expectedResult, ph.text)
        ## Save result page as an image
        self.BROWSER.get_screenshot_as_file('/results/' + v1 + '_divide_by_' + v2 + '.png')
        time.sleep(2)

    def test_10_divide_5(self):
        self.BaseTestSimpleDivision('10', '5', '2.00')

    def test_512_divide_8(self):
        self.BaseTestSimpleDivision('512', '8', '64.00')

    def test_100_divide_3(self):
        self.BaseTestSimpleDivision('100', '3', '33.33')

if __name__ == '__main__':
    unittest.main()