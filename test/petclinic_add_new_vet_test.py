import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class PetclinicAddNewVetTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

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
        self.assertNotEqual(actual_url, expected_url)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
