Feature: Publication Grid

  Background: Go to the Publication Grid page
    Given open numerator home page
    And Click on subscription management
    And click on Publication

  Scenario: Verify the publication page
    Given User in the publication page
    Then check the publication page visibility

  Scenario: Verify all existing publications in the Database
    Given User in the publication page
    Then check the total record count visibility

  Scenario: Verify that user is able to see all columns
    Given User in the publication page
    Then check the column visibilty

  Scenario: Verify that user is able to see total record count
    Given User in the publication page
    Then check the total record count visibility

    Scenario: Verify that filter funnel is displayed on each column
    Given User in the publication page
    Then check the filter funnel visibility on every column

  Scenario: Verify the pagination feature visibility
    Given User in the publication page
    Then should be able to see the pagination feature on the page bottom

  Scenario: Verify that the user is able to see the Add publication button
    Given User in the publication page
    Then should be able to see the Add publication button

  Scenario: Verify that the user is able to see Add Publication button tool-tip text
    Given User in the publication page
    When user clicks on the Add publication button
    Then should be able to see Add publication button tool-tip text

   Scenario: Verify the filter functionality
    Given User in the publication page
     Then check the filter functionality of every column

  @foo
  Scenario: Verify the Sorting functionality
    Given User in the publication page
    Then check the sorting functionality of every column


  Scenario: Verify the pagination feature
    Given User in the publication page
    When Clicked on the Page size
    Then Click on the page number
    And verify the total counts at the bottom of the page