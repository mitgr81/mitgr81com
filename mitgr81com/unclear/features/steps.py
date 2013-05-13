from lettuce import *
from lettuce.django import django_url
from splinter.browser import Browser
from nose.tools import assert_equals, assert_true

urls = {'unclear': django_url('/unclear/')}


@before.all
def set_browser():
    world.browser = Browser('phantomjs')


@after.all
def teardown(total):
    world.browser.quit()


@step(r'I browse to the "([^"]*)" page')
def access_url(step, page_name):
    world.browser.visit(urls[page_name])


@step(u'I enter "([^"]*)" in the "([^"]*)" field')
def type_into_field(step, text, field_name):
    world.browser.fill(field_name, text)


@step(u'I click the "([^"]*)" button')
def click_button(step, button_name):
    world.browser.find_by_name(button_name).first.click()


@step(u'I see the text "([^"]*)"')
def verify_text_present(step, text):
    assert_true(world.browser.is_text_present(text), "Did not see the text '{}' on the page.".format(text))


@step(u'I capture the unclear URI')
def capture_unclear_uri(step):
    world.last_unclear_uri = world.browser.find_by_id('unclear-uri').first.text
    print("Captured unclear_uri: {}".format(world.last_unclear_uri))
    print("Captured unclear_uri: {}".format(world.last_unclear_uri))
