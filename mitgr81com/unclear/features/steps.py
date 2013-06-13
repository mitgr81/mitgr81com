from lettuce import *
from splinter.browser import Browser
from splinter.request_handler.status_code import HttpResponseError
from nose.tools import assert_equals, assert_true, assert_not_equals

# urls = {'unclear': django_url('/unclear/')}
urls = {'unclear': 'http://localhost:5000/unclear/'}


@before.all
def set_browser():
    world.browser = Browser('chrome')


@after.all
def teardown(total):
    world.browser.quit()


@step(r'I browse to the "([^"]*)" page')
def access_url(step, page_name):
    world.browser.visit(urls[page_name])


@step(u'I browse to the last unclear page')
def access_last_url(step):
    world.browser.visit(world.last_unclear_uri)

@step(u'I fail to browse to the last unclear page')
def fail_to_access_last_url(step):
    try:
        world.browser.visit(world.last_unclear_uri)
    except HttpResponseError as e:
        assert_equals(404, e.status_code)
        return
    assert_not_equals(200, world.browser.status_code.code)


@step(u'I enter "([^"]*)" in the "([^"]*)" field')
def type_into_field(step, text, field_name):
    world.browser.fill(field_name, text)


@step(u'"([^"]*)" is in the "([^"]*)" field')
def verify_field_contents(step, text, field_name):
    assert_equals(text, world.browser.find_by_name(field_name).first.value)


@step(u'"([^"]*)" is not in the "([^"]*)" field')
def verify_field_contents_do_not_match(step, text, field_name):
    assert_not_equals(text, world.browser.find_by_name(field_name).first.value)


@step(u'I click the "([^"]*)" button')
def click_button(step, button_name):
    world.browser.find_by_name(button_name).first.click()


@step(u'I see the text "([^"]*)"')
def verify_text_present(step, text):
    assert_true(world.browser.is_text_present(text), "Did not see the text '{}' on the page.".format(text))


@step(u'I capture the unclear URI')
def capture_unclear_uri(step):
    world.last_unclear_uri = world.browser.find_by_id('unclear-uri').first.text
