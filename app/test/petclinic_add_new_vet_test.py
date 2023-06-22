import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import config


class PetclinicAddNewVetTest(unittest.TestCase):
    def setUp(self):
        if config.get("selenium_web_driver") == "firefox":
            self.driver = webdriver.Firefox()
        elif config.get("selenium_web_driver") == "edge":
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

    #    Feature: Create New Veterinarian
    #
    #    Scenario: Add a new veterinarian
    #        Given I am on the home page
    #        When I click on the "VETERINARIANS" navigation menu
    #        Then a menu with options "ALL" and "ADD NEW" should be displayed
    #        When I click on the "ADD NEW" option
    #        Then it should display the add veterinarians view
    #        When I fill out the new vet form with the following details:
    #            | First Name | Last Name | Specialty |
    #            | Daniel     | Galvis    | 1: Object |
    #        And I click on the save vet button
    #        Then it should redirect me to the vets table view
    #        And I should see the newly created vet in the table
    def test_add_new_vet(self):
        # Open web application
        self.driver.get("http://localhost:4400")

        new_vet = {"firstName": "Daniel", "lastName": "Galvis", "specialties": "1: Object"}

        time.sleep(2)

        # Open drop down to find button to navigate
        element = self.driver.find_elements(By.CSS_SELECTOR, "a.dropdown-toggle")
        element[1].click()

        time.sleep(2)

        # Click search owner butto to navigate to /vets/add
        continue_link = self.driver.find_element(By.LINK_TEXT, "ADD NEW")
        continue_link.click()

        time.sleep(1)

        # Find add vet form
        add_vet_form = self.driver.find_element(By.ID, "vet")
        for key, value in new_vet.items():
            html_input = add_vet_form.find_element(By.ID, key)
            if key == "specialties":
                all_options = html_input.find_elements(By.TAG_NAME, "option")
                for option in all_options:
                    if option.get_attribute("value") == value:
                        option.click()
            else:
                html_input.send_keys(value)

        time.sleep(1)

        form_buttons = add_vet_form.find_elements(By.TAG_NAME, "button")
        form_buttons[1].click()

        time.sleep(1)

        actual_url = self.driver.current_url
        expected_url = "http://localhost:4400/petclinic/vets"

        # Interface create new vet does not work
        self.assertEqual(actual_url, expected_url)

    # Feature: Create New Veterinarian with wrong information
    #
    #  Scenario: Add a new veterinarian with wrong information
    #    Given I am on the home page
    #    When I click on the "VETERINARIANS" navigation menu
    #    Then a menu with options "ALL" and "ADD NEW" should be displayed
    #    When I click on the "ADD NEW" option
    #    Then it should display the add veterinarians view
    #    When I fill out the new vet form with invalid data
    #    And I click on the save vet button
    #    Then it should show validation errors for the input fields
    def test_add_new_vet_with_wrong_data(self):
        self.driver.get("http://localhost:4400")

        new_vet = {"firstName": "a", "lastName": "a", "specialties": "1: Object"}

        time.sleep(2)

        # Open drop down to find button to navigate
        element = self.driver.find_elements(By.CSS_SELECTOR, "a.dropdown-toggle")
        element[1].click()

        time.sleep(2)

        # Click search owner butto to navigate to /vets/add
        continue_link = self.driver.find_element(By.LINK_TEXT, "ADD NEW")
        continue_link.click()

        time.sleep(1)

        # Find add vet form
        add_vet_form = self.driver.find_element(By.ID, "vet")
        for key, value in new_vet.items():
            html_input = add_vet_form.find_element(By.ID, key)
            if key == "specialties":
                all_options = html_input.find_elements(By.TAG_NAME, "option")
                for option in all_options:
                    if option.get_attribute("value") == value:
                        option.click()
            else:
                html_input.send_keys(value)

        time.sleep(1)

        form_buttons = add_vet_form.find_elements(By.TAG_NAME, "button")
        form_buttons[1].click()

        time.sleep(1)

        name_input = add_vet_form.find_element(By.ID, "firstName")
        last_name_input = add_vet_form.find_element(By.ID, "lastName")

        name_classes = name_input.get_attribute("class").split(" ")
        last_name_classes = last_name_input.get_attribute("class").split(" ")

        # Interface create new vet does not work
        self.assertIn("ng-invalid", name_classes)
        self.assertIn("ng-invalid", last_name_classes)

    # Feature: Create New Veterinarian with wrong information
    #
    #  Scenario: Add a new veterinarian with wrong information
    #    Given I am on the home page
    #    When I click on the "VETERINARIANS" navigation menu
    #    Then a menu with options "ALL" and "ADD NEW" should be displayed
    #    When I click on the "ADD NEW" option
    #    Then it should display the add veterinarians view
    #    When I fill out the new vet form with invalid alphanumeric data
    #    And I click on the save vet button
    #    Then it should show validation errors for the first name and last name fields
    def test_add_new_vet_with_alpha_num_data(self):
        self.driver.get("http://localhost:4400")

        new_vet = {"firstName": "a213213", "lastName": "a12321312", "specialties": "1: Object"}

        time.sleep(2)

        # Open drop down to find button to navigate
        element = self.driver.find_elements(By.CSS_SELECTOR, "a.dropdown-toggle")
        element[1].click()

        time.sleep(2)

        # Click search owner butto to navigate to /vets/add
        continue_link = self.driver.find_element(By.LINK_TEXT, "ADD NEW")
        continue_link.click()

        time.sleep(1)

        # Find add vet form
        add_vet_form = self.driver.find_element(By.ID, "vet")
        for key, value in new_vet.items():
            html_input = add_vet_form.find_element(By.ID, key)
            if key == "specialties":
                all_options = html_input.find_elements(By.TAG_NAME, "option")
                for option in all_options:
                    if option.get_attribute("value") == value:
                        option.click()
            else:
                html_input.send_keys(value)

        time.sleep(1)

        form_buttons = add_vet_form.find_elements(By.TAG_NAME, "button")
        form_buttons[1].click()

        time.sleep(1)

        name_input = add_vet_form.find_element(By.ID, "firstName")
        last_name_input = add_vet_form.find_element(By.ID, "lastName")

        name_classes = name_input.get_attribute("class").split(" ")
        last_name_classes = last_name_input.get_attribute("class").split(" ")

        # Interface create new vet does not work
        self.assertIn("ng-invalid", name_classes)
        self.assertIn("ng-invalid", last_name_classes)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
