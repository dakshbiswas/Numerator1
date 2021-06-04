Feature: Publication Grid

  Background: Go to the Publication Grid page
    Given open numerator home page for Publication grid
    And Click on subscription management for Publication grid
    And click on "01" Option for Publication grid

#    @tag
  Scenario: Verify the publication page
    Given "Publication List" page is displayed to the user
#@tag
  Scenario: Verify existing publications in the Database
    Then check for an existing record for publication grid
#@tag
  Scenario Outline: User validates columns in Subscription Grid
    Given User verifies "<columns>" as "<input_id>" field
  Examples:
  |  columns                |  input_id  |
  | Publication Code        |     01     |
  | Publication Name        |     02     |
  | Created On              |     03     |
  | Created By              |     04     |
  | Modified On             |     05     |
  | Modified By             |     06     |

#    @tag
  Scenario: Verify that user is able to see total record count
    Then check the total record count visibility in publication grid

# @tag
  Scenario: Pagination Test in Publication Grid
     When User understands that Total Count is More than Page Size in Publication Grid
     Then User tries to check if all pages are accessible properly in Publication Grid

  @Page_Size
#    @tag
  Scenario Outline: Page Size Test in Publication Grid
    When User clicks on page size in Publication Grid
    Then User clicks on page size value "<page_size>" in Publication Grid
    And Publication List page is loaded on page size value "<page_size>" in Publication Grid
    And User checks page size related changes on "<input_id>" UI in Publication Grid
     Examples:
        | page_size |  input_id |
        |  25       |    05     |
        |  50       |    05     |
        |  75       |    05     |
        |  100      |    05     |

#    @tag
  Scenario: Verify that the user is able to see the Add publication button
    Then User verifies the visibility of the Add publication button of publication grid
#@tag
  Scenario: Verify that the user is able to see Add Publication button tool-tip text
    When user hovers over the Add Publication button of publication grid
    Then User should be able to see Add publication button tool-tip text of publication grid

#    @tag
      Scenario Outline: User validates sorting feature in Publication Grid
    Then User double clicks on "<input_id>" field for Ascending Sort in Publication Grid
    And verifies the change on "<input_id>" after Ascending sort in Publication Grid
    And again User double clicks on "<input_id>" field for Descending Sort in Publication Grid
    And again verifies the change on "<input_id>" after Descending sort in Publication Grid
      Examples:
        |  input_id  |
        |  01        |
        |  02        |
        |  03        |
        |  04        |
        |  05        |
        |  06        |

 Scenario Outline: User validates filter feature in Publication Grid
   Then User clicks filter button on "<input_id>" field and enters "<criteria>" in Publication Grid
   And user clicks filter button in Publication Grid
   And verifies whether the "<input_id>" field is filtered in Publication Grid
   And User clicks filter button on "<input_id>" field in Publication Grid
   And user clicks clear button in Publication Grid
   And verifies whether the field is cleared in Publication Grid
      Examples:
        |  input_id  |   criteria  |
        |  01        |  Code       |
        |  02        |  Test       |
        |  04        |  admin      |
        |  06        |  admin      |

      @tag
  Scenario Outline: User validates filter feature of date in Publication Grid
    Then User clicks filter button on "<input_id>" field in Publication Grid
    And user clicks on date button with "<input_id>" in Publication Grid
    And User clicks down and enter in Publication Grid
    And user clicks filter button in Publication Grid
    And verifies whether the "<input_id>" date field is filtered in Publication Grid
    And User clicks filter button on "<input_id>" field in Publication Grid
    And user clicks clear button in Publication Grid
    And verifies whether the field is cleared in Publication Grid
        Examples:
        |  input_id  |
        |  03        |
        |  05        |