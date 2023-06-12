import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open web application
driver.get('http://localhost:4400')

new_vet = {"firstName": "Daniel", "lastName": "Galvis", "specialties":"1: Object"}

time.sleep(2)

# Open drop down to find button to navigate
element = driver.find_elements(By.CSS_SELECTOR, "a.dropdown-toggle")
element[1].click()

time.sleep(2)

# Click search owner butto to navigate to /vets/add
continue_link = driver.find_element(By.LINK_TEXT, 'ADD NEW')
continue_link.click()

time.sleep(1)

# Find add vet form
add_vet_form = driver.find_element(By.ID, "vet")
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

time.sleep(3)

# Verificar el resultado de la prueba
actual_url = driver.current_url
expected_url = 'http://localhost:4400/petclinic/vets'

if actual_url == expected_url:
    print("##############################################################")
    print('La prueba de registro de veterinarios ha pasado exitosamente.')
    print("##############################################################")
else:
    print("###########################################################")
    print('La prueba de registro de veterinarios ha fallado.')
    print("###########################################################")
