import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import page
import time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.python.org")

    def test_example(self):
        print("Test 1")
        assert True

    # def test_example2(self):
    #     print("Test 2")
    #     assert False
    # def test_title(self):
    #     mainPage=page.MainPage()
    #     assert mainPage.is_title_match()

    def test_search_python(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text_element="pycon"  
        mainPage.click_go_button()
        search_result_page=page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

if __name__=="__main__":
    unittest.main()