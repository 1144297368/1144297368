import unittest
from selenium import webdriver
from time import sleep
class MyTestCase(unittest.TestCase):
    driver = webdriver.Chrome(r'C:\Users\德玛西亚\Desktop\web自动化\chromedriver.exe')
    @classmethod
    def setUpClass(cls) -> None:
        MyTestCase.driver.get('https://www.ctrip.com/')
    @classmethod
    def tearDownClass(cls) -> None:
        MyTestCase.driver.quit()
    def setUp(self) -> None:
        sleep(2)
    def test_001(self):
        MyTestCase.driver.find_element_by_id('_allSearchKeyword').send_keys('太原')
    def test_002(self):
        MyTestCase.driver.find_element_by_id('search_button_global').click()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_001"))
    suite.addTest(MyTestCase("test_002"))
    unittest.TestRunner().run(suite)