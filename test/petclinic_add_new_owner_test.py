import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Ruta de validación crear dueño de mascota

# 1. Abrir home page.
# 2. Dar click en el menú de navegación en la opción `owners`.
# 3. Se debe desplegar un menú de dos opciones, con la opción `search` y `add new`.
# 4. Se hace click en la opción de `add new`, que nos llevará a la vista de crear nuevo dueño.
# 5. Llenamos los datos del formulario para crear un nuevo dueño
# 6. Damos click en el boton de `add owner`, esto nos llevara de nuevo a la vista de busqueda
# 7. Ingresaremos el criterio de busqueda en el input del formulario `Triana`.
# 6. Damos click en el boton de buscar, se cargará en la tabla la información filtada por el criterio de busqueda.
# 7. Damos click en el registro insertado filtrado en la tabla para ver la información del dueño creado.


class PetclinicAddNewOwnerTest(unittest.TestCase):
    def setUp(self):
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
