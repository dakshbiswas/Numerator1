Feature: Recipient Grid

  Background: Go to the Recipient Grid page
    Given open numerator home page for Recipient grid
    And Click on subscription management for Recipient grid
    And click on "04" Option for Recipient grid

#    @tag
  Scenario: Verify the Recipient page
    Given "Recipient List" page is displayed to the user for Recipient grid
#@tag
  Scenario: Verify existing Recipients in the Database
    Then check for an existing record in Recipient grid
#@tag
  Scenario Outline: User validates columns in Subscription Grid
    Given User verifies "<columns>" as "<input_id>" field for Recipient grid
  Examples:
  |  columns        |  input_id  |
  | Recipient Name  |     01     |
  | Address         |     02     |
  | Primary Phone   |     03     |
  | Backup Phone    |     04     |
  | Email           |     05     |
  | Monthly Cost    |     06     |

#    @tag
  Scenario: Verify that user is able to see total record count
    Then check the total record count visibility in Recipient grid

# @tag
  Scenario: Pagination Test in Recipient Grid
     When User understands that Total Count is More than Page Size in Recipient Grid
     Then User tries to check if all pages are accessible properly in Recipient Grid

  @Page_Size
#    @tag
  Scenario Outline: Page Size Test in Recipient Grid
    When User clicks on page size in Recipient Grid
    Then User clicks on page size value "<page_size>" in Recipient Grid
    And Publication List page is loaded on page size value "<page_size>" in Recipient Grid
    And User checks page size related changes on "<input_id>" UI in Recipient Grid
     Examples:
        | page_size |  input_id |
        |  25       |    05     |
        |  50       |    05     |
        |  75       |    05     |
        |  100      |    05     |

#    @tag
  Scenario: Verify that the user is able to see the Add Recipient button
    Then User verifies the visibility of the Add Recipient button of Recipient grid
#@tag
  Scenario: Verify that the user is able to see Add Publication button tool-tip text
    When user hovers over the Add Recipient button of Recipient grid
    Then User should be able to see Add Recipient button tool-tip text of Recipient grid

#    @tag
      Scenario Outline: User validates sorting feature in Recipient Grid
    Then User double clicks on "<input_id>" field for Ascending Sort in Recipient Grid
    And verifies the change on "<input_id>" after Ascending sort in Recipient Grid
    And again User double clicks on "<input_id>" field for Descending Sort in Recipient Grid
    And again verifies the change on "<input_id>" after Descending sort in Recipient Grid
      Examples:
        |  input_id  |
        |  01        |
        |  02        |
        |  03        |
        |  04        |
        |  05        |
        |  06        |
#@tag
 Scenario Outline: User validates filter feature in Recipient Grid
   Then User clicks filter button on "<input_id>" field and enters "<criteria>" in Recipient Grid
   And user clicks filter button in Recipient Grid
   And verifies whether the "<input_id>" field is filtered in Recipient Grid
   And User clicks filter button on "<input_id>" field in Recipient Grid
   And user clicks clear button in Recipient Grid
   And verifies whether the field is cleared in Recipient Grid
      Examples:
        |  input_id  | criteria |
        |  01        |  Jerry   |
        |  02        |  Test    |
        |  03        |  345678  |
        |  04        |  1234    |
        |  05        |  @test   |
        |  06        |  100     |