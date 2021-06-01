Feature: Recipient Grid

  Background: Go to the Recipient Grid page
    Given open numerator home page
    And Click on subscription management
    And click on Recipient

  Scenario: Verify the Recipient page
    Given User in the Recipient list page
    Then check the Recipient list page visibility

  Scenario: Verify all existing Recipients in the Database
    Given User in the Recipient list page
    Then check the total record count visibility of the recipient grid

  Scenario: Verify that user is able to see all columns in the recipient grid
     Given User in the Recipient list page
    Then check the column visibilty of the recipient grid

  Scenario: Verify that user is able to see total record count of the recipient grid
    Given User in the Recipient list page
    Then check the total record count visibility of the recipient grid

    Scenario: Verify that filter funnel is displayed on each column of the recipient grid
    Given User in the Recipient list page
    Then check the filter funnel visibility on every column of the recipient grid

  Scenario: Verify the pagination feature visibility of the recipient grid
    Given User in the Recipient list page
    Then should be able to see the pagination feature of the recipient grid

  Scenario: Verify that the user is able to see the Add Recipient button
    Given User in the Recipient list page
    Then should be able to see the Add Recipient button of the recipient grid

  Scenario: Verify that the user is able to see Add Recipient button tool-tip text
    Given User in the Recipient list page
    When user hovers over the Add Recipient button
    Then should be able to see Add Recipient button tool-tip text
 @tag
   Scenario: Verify the filter functionality in the recipient grid
    Given User in the Recipient list page
     Then enter "Jerry" in the Recipient Name filter
     Then enter "Test" in the Address filter
     Then enter "345678" in the primary phone filter
     Then enter "1234" in the backup phone filter
     Then enter "@test" in the email filter
     Then enter "100" in the Monthly cost filter
@tag
  Scenario: Verify the Sorting functionality in the recipient grid
    Given User in the Recipient list page
    Then check the sorting functionality of every column in the recipient grid

@tag
  Scenario: Verify the pagination feature in the recipient grid
    Given User in the Recipient list page
    When Clicked on the Page size in the recipient grid
    Then Click on the page number in the recipient grid
    And verify the total counts at the bottom of the page in the recipient grid