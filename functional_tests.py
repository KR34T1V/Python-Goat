from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Tom goes to view a new to-do list website. He lands on the homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and a header mention "to-do lists".
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # He is invited to add an item straight away.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'), 'Enter a to-do item'
        )
        # He types in "Get Fresh Tomatoes" as his first entry and presses enter.
        input_box.send_keys('Get Fresh Tomatoes')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # The page updates and now lists "get tomatoes" as a item in the to-do list.
        table = self.browser.find_element_by_id('id_list_table')
        row = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Get Fresh Tomatoes' for rows in rows)
        )
        # Below that there is an empty text box inviting him to add another item to the list.
        # He enters "prepare tomatoes". Tom has a pretty bland diet.
        # The page updates again and now displays "get tomatoes" & "prepare tomatoes" as to-do list items.
        # Of course there is another empty text box to add more items to the list.
        # Tom is afraid to close the page, for fear of losing his list.
        # Then he notices a button that allows him to generate a unique URL for his list. --there is some text explaining it.
        # He generates the URL and visits the link... HUZZA! His list is displayed again with all his items listed.
        # Satisfied, Tom closes the browser and takes a nap.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')