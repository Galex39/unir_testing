import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Ruta de validación para buscar dueño

# 1. Abrir home page.
# 2. Dar click en el menú de navegación en la opción `owners`.
# 3. Se debe desplegar un menú de dos opciones, con la opción `search` y `add new`.
# 4. Se hace click en la opción de search, que nos llevará a la vista de busqueda de dueños.
# 5. Ingresaremos el criterio de busqueda el input del formulario el cul es un apellido.
# 6. Damos click en el boton de buscar, se cargará en la tabla la información filtada por el criterio de busqueda.
# 7. Damos click en uno de los regsitros filtrados en la tabla para ver la información de un dueño especifico.


class PetclinicSearchOwnerTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_owner(self):
        owner = {
            "fullName": "Betty Davis",
            "address": "638 Cardinal Ave.",
            "city": "Sun Prairie",
            "telephone": "6085551749",
        }

        # Open web application
        self.driver.get("http://localhost:4400")

        time.sleep(2)

        # Open drop down to find button to navigate
        element = self.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle")
        element.click()

        time.sleep(1)

        # Click search owner butto to navigate to /owners
        continue_link = self.driver.find_element(By.LINK_TEXT, "SEARCH")
        continue_link.click()

        time.sleep(1)

        # Find search form
        search_form = self.driver.find_element(By.ID, "search-owner-form")

        # Getting search input and send search criteria
        search_input = search_form.find_element(By.ID, "lastName")
        search_input.send_keys("Davis")

        time.sleep(2)

        # Clicking search button
        search_button = search_form.find_element(By.TAG_NAME, "button")
        search_button.click()

        time.sleep(1)

        # Find table and find row
        owners_table = self.driver.find_element(By.ID, "ownersTable")
        owner_links = owners_table.find_elements(By.TAG_NAME, "a")
        owner_links[0].click()
        time.sleep(1)

        # Verify owner data
        owner_detailed_info = self.driver.find_element(By.TAG_NAME, "table")
        owner_information = owner_detailed_info.find_elements(By.TAG_NAME, "td")

        self.assertEqual(owner_information[0].text, owner.get("fullName"))
        self.assertEqual(owner_information[1].text, owner.get("address"))
        self.assertEqual(owner_information[2].text, owner.get("city"))
        self.assertEqual(owner_information[3].text, owner.get("telephone"))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
