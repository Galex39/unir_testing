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


driver = webdriver.Chrome()

# Open web application
driver.get('http://localhost:4400')

time.sleep(2)

# Open drop down to find button to navigate
element = driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle")
element.click()

time.sleep(1)

# Click search owner butto to navigate to /owners
continue_link = driver.find_element(By.LINK_TEXT, 'SEARCH')
continue_link.click()

time.sleep(1)

# Find search form
search_form = driver.find_element(By.ID, "search-owner-form")

# Getting search input and send search criteria
search_input = search_form.find_element(By.ID, "lastName")
search_input.send_keys("Davis")

time.sleep(2)

# Clicking search button
search_button = search_form.find_element(By.TAG_NAME, "button")
search_button.click()

time.sleep(1)

# Find table and find row
owners_table = driver.find_element(By.ID, "ownersTable")
owner_links = owners_table.find_elements(By.TAG_NAME, "a")
owner_links[0].click()

time.sleep(3)

# close
driver.quit()