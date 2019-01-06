from selenium import webdriver
import unittest

class NewUserTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_startAppLists(self):
        # Edith has heard about a cool new online to-do app. She goes         
        # to check out its homepage         
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists 
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finishing unit test...')

        # She is invited to enter to-do items


if __name__ == "__main__":
    unittest.main(warnings='ignore')
