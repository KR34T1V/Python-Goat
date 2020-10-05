from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        # He types in "Get Fresh Tomatoes" as his first entry and presses Enter.
        input_box.send_keys('Get Fresh Tomatoes')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # The page updates and now lists "Get Fresh Tomatoes" as a item in the to-do list.
        self.check_for_row_in_list_table('1: Get Fresh Tomatoes')

        # Below that there is an empty text box inviting him to add another item to the list.
        # He enters "Prepare Fresh Tomatoes". Tom has a pretty bland diet.
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Prepare Fresh Tomatoes')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now displays "Get Fresh Tomatoes" & "Prepare Fresh Tomatoes" as to-do list items.
        self.check_for_row_in_list_table('1: Get Fresh Tomatoes')
        self.check_for_row_in_list_table('2: Prepare Fresh Tomatoes')
        
        # Of course there is another empty text box to add more items to the list.
        # Tom is afraid to close the page, for fear of losing his list.
        # Then he notices a button that allows him to generate a unique URL for his list. --there is some text explaining it.
        # He generates the URL and visits the link... HUZZA! His list is displayed again with all his items listed.
        # Satisfied, Tom closes the browser and takes a nap.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')