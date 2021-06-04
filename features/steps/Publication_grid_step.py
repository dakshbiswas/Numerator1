from behave import *

from pageactions.NumColVisibilty import NumColVisibility
from pageactions.NumConfigs import NumConfigs
from pageactions.NumFilterFeatures import NumFilterFeatures
from pageactions.NumSortFeatures import NumSortFeatures

@given(u'open numerator home page for Publication grid')
def step_impl(context):
    # Instantiate Data Grid Features
    context.page = NumConfigs(context)
    context.page.visit_url(context.url)
    # Instantiate Sort Features
    context.sort = NumSortFeatures(context)

    # Instantiate Sort Features
    context.filter = NumFilterFeatures(context)

    context.col = NumColVisibility(context)

@given(u'Click on subscription management for Publication grid')
def click_on_subscription_management(context):
    context.page.click_on_subscription_management()

@given(u'click on "{input_id}" Option for Publication grid')
def step_impl(context, input_id):
    context.page.subscription_mgmt_option(input_id)


@given(u'"{sub_list}" page is displayed to the user')
def step_impl(context, sub_list):
    context.page.check_subscription_list_page(sub_list)

@then(u'check for an existing record for publication grid')
def step_impl(context):
    context.page.check_existing_record()

@given(u'User verifies "{col_name}" as "{id}" field')
def step_impl(context, col_name, id):
    context.col.check_columns_visibility(col_name, id)

@then(u'check the total record count visibility in publication grid')
def step_impl(context):
    context.page.check_total_count()
#
# @given(u'User verifies filter icon as "{id}" column')
# def step_impl(context, id):
#     context.page.check_filter_visibility(id)

@when(u'User understands that Total Count is More than Page Size in Publication Grid')
def step_impl(context):
    context.total = context.page.get_total_count()
    context.page_value = context.page.get_page_size()
    assert context.total > context.page_value

@then(u'User tries to check if all pages are accessible properly in Publication Grid')
def step_impl(context):
    context.page.PaginationOnSubscriptionGrid(context.total, context.page_value)


@when(u'User clicks on page size in Publication Grid')
def step_impl(context):
    context.page.click_page_size()


@then(u'User clicks on page size value "{page_size}" in Publication Grid')
def step_impl(context, page_size):
    context.page.click_page_size_value(page_size)


@then(u'Publication List page is loaded on page size value "{page_size}" in Publication Grid')
def step_impl(context, page_size):
    context.page.compare_page_length(page_size)


@then(u'User checks page size related changes on "{input_id}" UI in Publication Grid')
def step_impl(context, input_id):
    context.page.check_page_length(input_id)


@then(u'User verifies the visibility of the Add publication button of publication grid')
def step_impl(context):
    context.page.check_add_publication()

@when(u'user hovers over the Add Publication button of publication grid')
def step_impl(context):
    context.page.add_hover()

@then(u'User should be able to see Add publication button tool-tip text of publication grid')
def step_impl(context):
    context.page.add_tool_visibility()

@then(u'User double clicks on "{input_id}" field for Ascending Sort in Publication Grid')
def step_impl(context, input_id):
    context.dataRow = context.page.getPublicationGridDataRowTextById(input_id)
    context.sort.sortByDoubleClickOnPublicationGrid(input_id)

@then(u'verifies the change on "{input_id}" after Ascending sort in Publication Grid')
def step_impl(context, input_id):
    assert context.dataRow != context.page.getPublicationGridDataRowTextById(input_id)

@then(u'again User double clicks on "{input_id}" field for Descending Sort in Publication Grid')
def step_impl(context, input_id):
    context.dataRow = context.page.getPublicationGridDataRowTextById(input_id)
    context.sort.sortByDoubleClickOnPublicationGrid(input_id)

@then(u'again verifies the change on "{input_id}" after Descending sort in Publication Grid')
def step_impl(context, input_id):
    assert context.dataRow != context.page.getPublicationGridDataRowTextById(input_id)

    # =================================================================

@then(u'User clicks filter button on "{input_id}" field and enters "{criteria}" in Publication Grid')
def clickFilterIconOnSubscriptionGrid(context, input_id, criteria):
    context.dataRow = criteria
    context.filter.clickFilterIconOnPublicationGrid(input_id, criteria)

@then(u'user clicks filter button in Publication Grid')
def step_impl(context):
    context.filter.clickFilterButtonOnPublicationGrid()

@then(u'User clicks filter button on "{input_id}" field in Publication Grid')
def step_impl(context, input_id):
    context.filter.clickFilterButtonOnColPublicationGrid(input_id)

@then(u'verifies whether the "{input_id}" field is filtered in Publication Grid')
def step_impl(context, input_id):
    # print("first =-=-=-=-= "+context.dataRow)
    # print("second =-=-=-=-= "+context.page.getPublicationGridDataRowTextById(input_id))
    assert context.dataRow in context.page.getPublicationGridDataRowTextById(input_id)

@then(u'user clicks clear button in Publication Grid')
def step_impl(context):
    context.totalCount = context.page.get_total_count()
    context.filter.clearFilterOnPublicationGrid()

@then(u'verifies whether the field is cleared in Publication Grid')
def step_impl(context):
    assert context.totalCount <= context.page.get_total_count()


    # -------------------------------------------------------------------

@then(u'user clicks on date button with "{input_id}" in Publication Grid')
def step_impl(context, input_id):
    context.filter.clickOnDateButton(input_id)

@then(u'User clicks down and enter in Publication Grid')
def step_impl(context):
    context.totalCount = context.page.get_total_count()
    context.filter.downEnter()

@then(u'verifies whether the "{input_id}" date field is filtered in Publication Grid')
def step_impl(context, input_id):
    assert context.totalCount >= context.page.get_total_count()
