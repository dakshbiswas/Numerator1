Feature: Edit Subscription

  Background: Go to the Subscription List page
    Given open numerator home page
    And Click on subscription management
    And click on subscription
    Then Double click on the record with "test ned" as subscription name


  Scenario: User is in the Edit Subscription page
    Then Verify Edit subscription screen

  Scenario: User is able to see the populated fields with existing values of the subscription
    Given User is in the Edit Subscription page
    Then verify the field subscription name has "test ned" already filled
    And Verify all the other fields

  Scenario: User is able to see the Transaction Grid
    Given User is in the Edit Subscription page
    Then check all the columns in the Transaction grid

  Scenario: User is able to see the Cancel and Save buttons in the Edit screen
    Given User is in the Edit Subscription page
    Then check the Cancel and save buttons visibility

  Scenario: User is able to see Edit the fields in the Edit screen and cancel it
    Given User is in the Edit Subscription page
    Then Edit the field Subscription name with "u" to cancel
    Then Click on the cancel button and verify

  Scenario: User is able to verify editing of duplicate user
    Given User is in the Edit Subscription page
    Then Edit the field Subscription name with duplicate "Times magazine"
    Then verify the message card "Duplicate Check: The record is already exists."
@tag
  Scenario: User is able to edit the fields on the Edit screen then save and verify
    Given User is in the Edit Subscription page
    Then Edit the field Subscription name with new data "test nedd"
    Then Edit the field Provider Name with "ABC Corporation"
    Then Edit the field Recipient Name with "ABC"
    Then Edit the field Login Info with "abc"
    Then Edit the field Notes with "testing"
    Then Click on the save button and verify with subscription name "test nedd"

