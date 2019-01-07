from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewUserTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_todoFeatures(self):
        # Sasha has heard about a cool new online to-do app. She goes         
        # to check out its homepage         
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter to-do items
        inputBox = self.browser.find_element_by_id('newitem-id')
        self.assertEqual(
            inputBox.get_attribute('placeholder'),
            'Enter To-Do item'
        )

        # She typed: "Buy peacock-leathered jacket"
        inputBox.send_keys("Buy peacock-leathered jacket")
        inputBox.send_keys(Keys.ENTER)
        time.sleep(1)

        # When she hits enter, the To-Do lists has her newly added items
        # Now the page lists has: "1. Buy peacock-leathered jacket"
        table = self.browser.find_element_by_id('todo-table-id')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("1. Buy peacock-leathered jacket", [row.text for row in rows])
        
        # She then add another items, she wanted to show off...
        inputBox.send_keys("Show off the jacket to friends")
        inputBox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Now page lists has "2. Show off jacket to friends"
        table = self. browser.find_element_by_id('todo-table-id')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn("2. Show off the jacket to friends", [row.text for row in rows])

        # Sasha is satisfied 
        self.fail('Finishing unit test...')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
