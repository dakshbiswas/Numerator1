from behave import *

from pageactions.NumColVisibilty import NumColVisibility
from pageactions.NumConfigs import NumConfigs
from pageactions.NumEditSubscription import NumEditSubscription

@given(u'open numerator home page for Subscription grid')
def step_impl(context):
    # Instantiate Data Grid Features
    context.page = NumConfigs(context)
    context.page.visit_url(context.url)
    context.edit = NumEditSubscription(context)
    context.col = NumColVisibility(context)

@given(u'Click on subscription management for Subscription grid')
def click_on_subscription_management(context):
    context.page.click_on_subscription_management()

@given(u'click on "{input_id}" Option for Subscription grid')
def step_impl(context, input_id):
    context.page.subscription_mgmt_option(input_id)

@then(u'Double click on the first record for Subscription grid')
def step_impl(context):
    context.page.doubleClickFirstRecordSub()

@given(u'"{edit_sub}" page is displayed to the user for Subscription grid')
def step_impl(context, edit_sub):
    context.page.check_edit_page(edit_sub)

@then(u'verify the field with "{id_01}" is already filled')
def step_impl(context, id_01):
    context.edit.check_if_already_filled(id_01)

@then(u'User verifies "{col_name}" as "{id}" field')
def step_impl(context, col_name, id):
    context.col.check_columns_visibility_edit_sub(col_name, id)

@then(u'Edit the data in field "{field}" with "{data}"')
def step_impl(context, field, data):
    context.edit.fill_data_in_field(field, data)

@then(u'Click on the save button and verify row with "{col_name}"')
def step_impl(context, col_name):
    context.edit.verify_save(col_name)

@then(u'Click on save button for Subscription grid')
def step_impl(context):
    context.edit.click_save()

@then(u'Click on the cancel button and verify row with "{col_name}"')
def step_impl(context, col_name):
    context.edit.verify_cancel(col_name)

@then(u'verify the message card "{msg}"')
def step_impl(context, msg):
    context.edit.verify_duplicate_msg(msg)