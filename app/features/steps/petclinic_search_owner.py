from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given("I am on the home page")
def step_given_i_am_on_the_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:4400")
    time.sleep(2)


@when('I click on the "owners" navigation menu')
def step_when_i_click_on_owners_navigation_menu(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle")
    element.click()
    time.sleep(1)


@then('a menu with options "search" and "add new" should be displayed')
def step_then_menu_with_options_search_and_add_new_should_be_displayed(context):
    expected_options = ["SEARCH", "ADD NEW"]
    search_link = context.driver.find_element(By.LINK_TEXT, "SEARCH")
    add_new_link = context.driver.find_element(By.LINK_TEXT, "ADD NEW")
    actual_options = [search_link.text, add_new_link.text]
    assert expected_options == actual_options


@when('I click on the "search" option')
def step_when_i_click_on_search_option(context):
    continue_link = context.driver.find_element(By.LINK_TEXT, "SEARCH")
    continue_link.click()
    time.sleep(1)


@then("I should be taken to the owner search view")
def step_then_i_should_be_taken_to_owner_search_view(context):
    assert context.driver.current_url.endswith("/owners")


@when('I enter the search criteria "{search_criteria}" in the input field')
def step_when_i_enter_search_criteria_in_input_field(context, search_criteria: str):
    search_input = context.driver.find_element(By.ID, "lastName")
    search_input.send_keys(search_criteria)
    time.sleep(2)


@when("I click the search button")
def step_when_i_click_search_button(context):
    search_form = context.driver.find_element(By.ID, "search-owner-form")
    search_button = search_form.find_element(By.TAG_NAME, "button")
    search_button.click()
    time.sleep(1)


@then("the table should be populated with owners filtered by the search criteria")
def step_then_table_should_be_populated_with_owners_filtered_by_search_criteria(context):
    owners_table = context.driver.find_element(By.ID, "ownersTable")
    rows = owners_table.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 1


@when("I click on one of the filtered records in the table")
def step_when_i_click_on_filtered_record_in_table(context):
    owners_table = context.driver.find_element(By.ID, "ownersTable")
    owner_links = owners_table.find_elements(By.TAG_NAME, "a")
    owner_links[0].click()
    time.sleep(1)


@then("I should see the details of the specific owner")
def step_then_i_should_see_details_of_specific_owner(context):
    owner_detailed_info = context.driver.find_element(By.TAG_NAME, "table")
    owner_information = owner_detailed_info.find_elements(By.TAG_NAME, "td")

    expected_owner = {
        "fullName": "Betty Davis",
        "address": "638 Cardinal Ave.",
        "city": "Sun Prairie",
        "telephone": "6085551749",
    }

    assert owner_information[0].text == expected_owner.get("fullName")
    assert owner_information[1].text == expected_owner.get("address")
    assert owner_information[2].text == expected_owner.get("city")
    assert owner_information[3].text == expected_owner.get("telephone")

    time.sleep(1)
