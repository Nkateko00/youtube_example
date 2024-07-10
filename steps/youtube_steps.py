from behave import *
from helper.youtube_helper import youtubeHelper


youtuber_helper = youtubeHelper()

@given(u'I am on the Youtube homepage')
def step_impl(context):
    youtuber_helper.youtube_homepage()


@when(u'I "{search}" for the vibes playlist on search bar')
def step_impl(context,search):
    youtuber_helper.searhing(search)

@then(u'I click  enter')
def step_impl(context):
    youtuber_helper.click_search_bar()


@then(u'I click on playlist to open')
def step_impl(context):
    youtuber_helper.click_playlist()
    


@then(u'I click on selected song')
def step_impl(context):
    youtuber_helper.click_song()


@then(u'I should get Vibes playlist displayed')
def step_impl(context):
    youtuber_helper.validate_search_results()