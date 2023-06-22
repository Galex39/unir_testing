Feature: Validating owner search

  Scenario: Searching for an owner
    Given I am on the home page
     When I click on the "owners" navigation menu
     Then a menu with options "search" and "add new" should be displayed
     When I click on the "search" option
     Then I should be taken to the owner search view
     When I enter the search criteria "Davis" in the input field
     And I click the search button
     Then the table should be populated with owners filtered by the search criteria
     When I click on one of the filtered records in the table
     Then I should see the details of the specific owner