from behave import *
from pageactions.RecipientPage import RecipientPage


@given(u'open numerator home page')
def step_impl(context):
    context.page = RecipientPage(context)
    context.page.visit_url(context.url)

@given(u'Click on subscription management')
def step_impl(context):
    context.page.click_on_subscription_management()

@given(u'click on Recipient')
def step_impl(context):
    context.page.click_on_recipient()

@given(u'User in the Recipient list page')
def step_impl(context):
    context.page.verify_recipient_page()

@then(u'check the Recipient list page visibility')
def step_impl(context):
    context.page.verify_recipient_page()

@then(u'check the total record count visibility of the recipient grid')
def step_impl(context):
    context.page.verify_record_count()

@then(u'check the column visibilty of the recipient grid')
def step_impl(context):
    context.page.verify_columns()


@then(u'check the filter funnel visibility on every column of the recipient grid')
def step_impl(context):
    context.page.verify_filter_display()


@then(u'should be able to see the pagination feature of the recipient grid')
def step_impl(context):
    context.page.page_visibilty()


@then(u'should be able to see the Add Recipient button of the recipient grid')
def step_impl(context):
    context.page.add_visibility()


@when(u'user hovers over the Add Recipient button')
def step_impl(context):
    context.page.add_visibility_hover()

@then(u'should be able to see Add Recipient button tool-tip text')
def step_impl(context):
    context.page.add_visibility_hover_check()


@then(u'enter "{data}" in the Recipient Name filter')
def step_impl(context, data):
    context.page.verify_recipient_filter(data)

@then(u'enter "{data}" in the Address filter')
def step_impl(context, data):
    context.page.verify_address_filter(data)


@then(u'enter "{data}" in the primary phone filter')
def step_impl(context, data):
    context.page.verify_primary_filter(data)


@then(u'enter "{data}" in the backup phone filter')
def step_impl(context, data):
    context.page.verify_backup_filter(data)


@then(u'enter "{data}" in the email filter')
def step_impl(context, data):
    context.page.verify_email_filter(data)


@then(u'enter "{data}" in the Monthly cost filter')
def step_impl(context, data):
    context.page.verify_cost_filter(data)


@then(u'check the sorting functionality of every column in the recipient grid')
def step_impl(context):
    context.page.verify_sorting()


@when(u'Clicked on the Page size in the recipient grid')
def step_impl(context):
    context.page.change_page_size()


@then(u'Click on the page number in the recipient grid')
def step_impl(context):
    context.page.next_page_feature()


@then(u'verify the total counts at the bottom of the page in the recipient grid')
def step_impl(context):
    context.page.verify_record_count()
