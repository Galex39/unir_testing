import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import config

# Feature: Validating owner creation
#
#   Scenario: Creating a new owner
#     Given I am on the home page
#     When I click on the "owners" navigation menu
#     Then a menu with options "search" and "add new" should be displayed
#     When I click on the "add new" option
#     Then I should be taken to the new owner creation view
#     When I fill in the form with the owner data
#     And I click the "add owner" button
#     Then I should be redirected to the search view
#     When I enter the search criteria "Triana" in the search input field
#     And I click the search button
#     Then the table should be populated with owners filtered by the search criteria
#     When I click on the inserted record in the table
#     Then I should see the information of the created owner


class PetclinicAddNewOwnerTest(unittest.TestCase):
    def setUp(self):
        if config.get("selenium_web_driver") == "firefox":
            self.driver = webdriver.Firefox()
        elif config.get("selenium_web_driver") == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

    def test_add_new_owner(self):
        new_owner = {
            "firstName": "Andrew",
            "lastName": "Triana",
            "address": "Av 45",
            "city": "New York",
            "telephone": "300912547",
        }

        # Open web application
        self.driver.get("http://localhost:4400")

        time.sleep(2)

        # Open drop down to find button to navigate
        element = self.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle")
        element.click()

        time.sleep(1)

        # Click search owner butto to navigate to /owners
        continue_link = self.driver.find_element(By.LINK_TEXT, "ADD NEW")
        continue_link.click()

        time.sleep(1)

        add_owner_form = self.driver.find_element(By.TAG_NAME, "form")

        for key, value in new_owner.items():
            html_input = add_owner_form.find_element(By.ID, key)
            html_input.send_keys(value)

        time.sleep(1)

        form_buttons = add_owner_form.find_elements(By.TAG_NAME, "button")
        form_buttons[1].click()

        time.sleep(1)

        # Find search form
        search_form = self.driver.find_element(By.ID, "search-owner-form")

        # Getting search input and send search criteria
        search_input = search_form.find_element(By.ID, "lastName")
        search_input.send_keys("Triana")

        time.sleep(2)

        # Clicking search button
        search_button = search_form.find_element(By.TAG_NAME, "button")
        search_button.click()

        time.sleep(2)

        # Find table and find row
        owners_table = self.driver.find_element(By.ID, "ownersTable")
        owner_links = owners_table.find_elements(By.TAG_NAME, "a")
        owner_links[0].click()

        # Verify inserted information
        owner_detailed_info = self.driver.find_element(By.TAG_NAME, "table")
        owner_information = owner_detailed_info.find_elements(By.TAG_NAME, "td")

        self.assertEqual(
            owner_information[0].text, f"{new_owner.get('firstName')} {new_owner.get('lastName')}"
        )
        self.assertEqual(owner_information[1].text, new_owner.get("address"))
        self.assertEqual(owner_information[2].text, new_owner.get("city"))
        self.assertEqual(owner_information[3].text, new_owner.get("telephone"))

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
