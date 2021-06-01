from behave import *
from pageactions.PublicationPage import PublicationPage

# @given(u'open numerator home page')
# def step_impl(context):
#     context.page = PublicationPage(context)
#     context.page.visit_url(context.url)
#
# @given(u'Click on subscription management')
# def step_impl(context):
#     context.page.click_on_subscription_management()

@given(u'click on Publication')
def step_impl(context):
    context.page.click_on_publication()

@given(u'User in the publication page')
def step_impl(context):
    pass

@then(u'check the publication page visibility')
def step_impl(context):
    context.page.verify_publication_page()

@then(u'check the total record count visibility')
def step_impl(context):
    context.page.verify_record_count()
    # pass

@then(u'check the column visibilty')
def step_impl(context):
    context.page.verify_columns()
    # pass

@then(u'check the filter funnel visibility on every column')
def step_impl(context):
    context.page.verify_filter_display()
    # pass

@then(u'should be able to see the pagination features on the page bottom')
def step_impl(context):
    context.page.page_visibilty()
    # pass

@then(u'should be able to see the Add publication button')
def step_impl(context):
    context.page.add_visibility()


@when(u'user clicks on the Add publication button')
def step_impl(context):
    context.page.add_visibility_click()
    # pass

@then(u'should be able to see Add publication button tool-tip text')
def step_impl(context):
    context.page.add_tool_visibility()
    # pass

@then(u'check the filter functionality of every column')
def step_impl(context):
    context.page.verify_filter_functionality()
    # pass

@then(u'check the sorting functionality of every column')
def step_impl(context):
    context.page.verify_sorting()
    # pass

@then(u'Click on the page number')
def step_impl(context):
    context.page.next_page_feature()
    # pass

@when(u'Clicked on the Page size')
def step_impl(context):
    context.page.change_page_size()
    # pass

@then(u'verify the total counts at the bottom of the page')
def step_impl(context):
    context.page.verify_record_count()
    # pass
