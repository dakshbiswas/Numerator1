Feature: Edit Subscription

  Background: Go to the Subscription List page
    Given open numerator home page for Subscription grid
    And Click on subscription management for Subscription grid
    And click on "05" Option for Subscription grid
    Then Double click on the first record for Subscription grid
#   @tag
  Scenario: verify the Edit Subscription page
    Given "Edit Subscription" page is displayed to the user for Subscription grid
#@tag
  Scenario: User is able to see the populated fields with existing values of the subscription gird
    Then verify the field with "01" is already filled
#@tag
  Scenario Outline: User validates columns in Subscription Grid
    Then User verifies "<columns>" as "<input_id>" field
  Examples:
  |  columns            |  input_id  |
  | Transaction Date    |     01     |
  | Start Date          |     02     |
  | End Date            |     03     |
  | Amount              |     04     |
  | Transaction Type    |     05     |
  | Notes               |     06     |
  | Recipient Name      |     07     |
#@tag
  Scenario Outline: User is able to see Edit the fields in the Edit screen and cancel it
    Then Edit the data in field "<id_01>" with "<data_01>"
    Then Edit the data in field "<id_04>" with "<data_04>"
    Then Edit the data in field "<id_05>" with "<data_05>"
    Then Click on the cancel button and verify row with "<data_01>"

      Examples:
   |  id_01   | data_01   |  id_04   | data_04   |  id_05   | data_05  |
   |   01     |   test    |   04     |   test    |   05     |   test   |
#@tag
  Scenario Outline: User is able to verify editing of duplicate user
    Then Edit the data in field "<id_01>" with "<data_01>"
    Then Click on save button for Subscription grid
    Then verify the message card "Duplicate Check: The record already exists."

     Examples:
    |  id_01  |    data_01     |
    |   01    | Times magazine |

@tag
  Scenario Outline: User is able to edit the fields on the Edit screen then save and verify
    Then Edit the data in field "<id_01>" with "<data_01>"
    Then Edit the data in field "<id_02>" with "<data_02>"
    Then Edit the data in field "<id_03>" with "<data_03>"
    Then Edit the data in field "<id_04>" with "<data_04>"
    Then Edit the data in field "<id_05>" with "<data_05>"
    Then Click on the save button and verify row with "<data_01>"

Examples:
  |  id_01   | data_01   |  id_02   | data_02   |  id_03   | data_03   |  id_04   | data_04   |  id_05   | data_05   |
  |   01     |   test 18 |   02     |   test    |   03     |   test    |   04     |   test    |   05     |   test    |

