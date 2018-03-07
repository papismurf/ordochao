from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import time, sleep


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jo heard about a cool new online To-Do app
        # So he goes online and checks the homepage
        self.browser.get("http://localhost:8000")
        
        # He notices the page title and header mention To-Do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
     #  self.fail("Finish the test!")
            
        # He is invited to enter a item To-do straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(

            inputbox.get_attribute('placeholder'),
            'Enter a to do item'
        )
        # He types "Buy food shopping" into a text box
        inputbox.send_keys('Buy food shopping')

        # When he hits enter, the page updates and now tlists
        # "1: Buy food shopping" as an item on a To-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertTrue(
            any(row.text == '1: Buy food shopping' for row in rows),
            "New to-do item did not appear in table"
        )
        # There is still a text box inviting him to enter another item. He
        # enters: "Buy Son baby grows"
        self.fail('Finish the test!')
        # The page updates and now shows both items on his list!

        # Jo wonders if the site will remember his list. Then he sees that
        # the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits thar URL - his To-do list is still there.

        # Satisfied, he goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings='ignore')
