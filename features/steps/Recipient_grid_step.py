from behave import *

from pageactions.NumColVisibilty import NumColVisibility
from pageactions.NumConfigs import NumConfigs
from pageactions.NumFilterFeatures import NumFilterFeatures
from pageactions.NumSortFeatures import NumSortFeatures

@given(u'open numerator home page for Recipient grid')
def step_impl(context):
    # Instantiate Data Grid Features
    context.page = NumConfigs(context)
    context.page.visit_url(context.url)
    # Instantiate Sort Features
    context.sort = NumSortFeatures(context)

    # Instantiate Sort Features
    context.filter = NumFilterFeatures(context)

    context.col = NumColVisibility(context)

@given(u'Click on subscription management for Recipient grid')
def click_on_subscription_management(context):
    context.page.click_on_subscription_management()

@given(u'click on "{input_id}" Option for Recipient grid')
def step_impl(context, input_id):
    context.page.subscription_mgmt_option(input_id)


@given(u'"{sub_list}" page is displayed to the user for Recipient grid')
def step_impl(context, sub_list):
    context.page.check_subscription_list_page(sub_list)

@then(u'check for an existing record in Recipient grid')
def step_impl(context):
    context.page.check_existing_record_for_recipient()

@given(u'User verifies "{col_name}" as "{id}" field for Recipient grid')
def step_impl(context, col_name, id):
    context.col.check_columns_visibility_recipient(col_name, id)

@then(u'check the total record count visibility in Recipient grid')
def step_impl(context):
    context.page.check_total_count()

@when(u'User understands that Total Count is More than Page Size in Recipient grid')
def step_impl(context):
    context.total = context.page.get_total_count()
    context.page_value = context.page.get_page_size()
    assert context.total > context.page_value

@then(u'User tries to check if all pages are accessible properly in Recipient grid')
def step_impl(context):
    context.page.PaginationOnSubscriptionGrid(context.total, context.page_value)


@when(u'User clicks on page size in Recipient grid')
def step_impl(context):
    context.page.click_page_size()


@then(u'User clicks on page size value "{page_size}" in Recipient grid')
def step_impl(context, page_size):
    context.page.click_page_size_value(page_size)


@then(u'Publication List page is loaded on page size value "{page_size}" in Recipient grid')
def step_impl(context, page_size):
    context.page.compare_page_length(page_size)


@then(u'User checks page size related changes on "{input_id}" UI in Recipient grid')
def step_impl(context, input_id):
    context.page.check_page_length(input_id)


@then(u'User verifies the visibility of the Add Recipient button of Recipient grid')
def step_impl(context):
    context.page.check_add_recipient()

@when(u'user hovers over the Add Recipient button of Recipient grid')
def step_impl(context):
    context.page.add_hover_recipient()

@then(u'User should be able to see Add Recipient button tool-tip text of Recipient grid')
def step_impl(context):
    context.page.add_tool_recipient_visibility()

@then(u'User double clicks on "{input_id}" field for Ascending Sort in Recipient Grid')
def step_impl(context, input_id):
    context.dataRow = context.page.getRecipientGridDataRowTextById(input_id)
    context.sort.sortByDoubleClickOnRecipientGrid(input_id)

@then(u'verifies the change on "{input_id}" after Ascending sort in Recipient Grid')
def step_impl(context, input_id):
    assert context.dataRow != context.page.getRecipientGridDataRowTextById(input_id)

@then(u'again User double clicks on "{input_id}" field for Descending Sort in Recipient Grid')
def step_impl(context, input_id):
    context.dataRow = context.page.getRecipientGridDataRowTextById(input_id)
    context.sort.sortByDoubleClickOnRecipientGrid(input_id)

@then(u'again verifies the change on "{input_id}" after Descending sort in Recipient Grid')
def step_impl(context, input_id):
    assert context.dataRow != context.page.getRecipientGridDataRowTextById(input_id)

    # =================================================================

@then(u'User clicks filter button on "{input_id}" field and enters "{criteria}" in Recipient Grid')
def clickFilterIconOnSubscriptionGrid(context, input_id, criteria):
    context.dataRow = criteria
    context.filter.clickFilterIconOnRecipientGrid(input_id, criteria)

@then(u'user clicks filter button in Recipient Grid')
def step_impl(context):
    context.filter.clickFilterButtonOnPublicationGrid()

@then(u'User clicks filter button on "{input_id}" field in Recipient Grid')
def step_impl(context, input_id):
    context.filter.clickFilterButtonOnColRecipientGrid(input_id)

@then(u'verifies whether the "{input_id}" field is filtered in Recipient Grid')
def step_impl(context, input_id):
    # print("first =-=-=-=-= "+context.dataRow)
    # print("second =-=-=-=-= "+context.page.getPublicationGridDataRowTextById(input_id))
    assert context.dataRow in context.page.getRecipientGridDataRowTextById(input_id)

@then(u'user clicks clear button in Recipient Grid')
def step_impl(context):
    context.totalCount = context.page.get_total_count()
    context.filter.clearFilterOnPublicationGrid()

@then(u'verifies whether the field is cleared in Recipient Grid')
def step_impl(context):
    assert context.totalCount <= context.page.get_total_count()
