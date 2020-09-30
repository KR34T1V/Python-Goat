from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Tom goes to view a new to-do list website. He lands on the homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title "to-do lists".
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # He is invited to add an item straight away.
        # He types in "get tomatoes" as his first entry and presses enter.
        # The page updates and now lists "get tomatoes" as a item in the to-do list.
        # Below that there is an empty text box inviting him to add another item to the list.
        # He enters "prepare tomatoes". Tom has a pretty bland diet.
        # The page updates again and now displays "get tomatoes" & "prepare tomatoes" as to-do list items.
        # Of course there is another empty text box to add more items to the list.
        # Tom is afraid to close the page, for fear of losing his list.
        # Then he notices a button that allows him to generate a unique URL for his list. --there is some text explaining it.
        # He generates the URL and visits the link... HAZZA! His list is displayed again with all his items listed.
        # Satisfied, Tom closes the browser and takes a nap.

if __name__ == '__main__':
    unittest.main(warnings='ignore')