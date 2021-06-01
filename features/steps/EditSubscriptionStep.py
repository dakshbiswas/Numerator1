from behave import *
from pageactions.EditSubscriptionPage import EditSubscriptionPage

# @given(u'open numerator home page')
# def step_impl(context):
#     context.page = EditSubscriptionPage(context)
#     context.page.visit_url(context.url)
#
# @given(u'Click on subscription management')
# def step_impl(context):
#     context.page.click_on_subscription_management()

@given(u'click on subscription')
def step_impl(context):
    context.page.click_on_subscription()

@then(u'Double click on the record with "test ned" as subscription name')
def step_impl(context):
    context.page.click_on_record()

@then(u'Verify Edit subscription screen')
def step_impl(context):
    context.page.verify_edit_page()

@given(u'User is in the Edit Subscription page')
def step_impl(context):
    context.page.verify_edit_page()

@then(u'verify the field subscription name has "{test}" already filled')
def step_impl(context, test):
    context.page.verify_filled_data(test)

@then(u'Verify all the other fields')
def step_impl(context):
    context.page.verify_all_fields()

@then(u'check all the columns in the Transaction grid')
def step_impl(context):
    context.page.verify_transaction_grid()

@then(u'check the Cancel and save buttons visibility')
def step_impl(context):
    context.page.verify_saveCancel()

@then(u'Edit the field Subscription name with "{test}" to cancel')
def step_impl(context, test):
    context.page.verify_edit(test)

@then(u'Click on the cancel button and verify')
def step_impl(context):
    context.page.verify_cancel()

@then(u'Edit the field Subscription name with duplicate "{data}"')
def step_impl(context, data):
    context.page.enter_duplicate_data(data)

@then(u'verify the message card "{msg}"')
def step_impl(context, msg):
    context.page.verify_duplicate_msg(msg)

@then(u'Edit the field Subscription name with new data "{data}"')
def step_impl(context, data):
    context.page.enter_new_subName(data)

@then(u'Edit the field Provider Name with "{data}"')
def step_impl(context, data):
    context.page.enter_new_proName(data)


@then(u'Edit the field Recipient Name with "{data}"')
def step_impl(context, data):
    context.page.enter_new_recName(data)


@then(u'Edit the field Login Info with "{data}"')
def step_impl(context, data):
    context.page.enter_new_info(data)


@then(u'Edit the field Notes with "{data}"')
def step_impl(context, data):
    context.page.enter_new_notes(data)


@then(u'Click on the save button and verify with subscription name "{data}"')
def step_impl(context, data):
    context.page.save_and_verify(data)

