from lettuce import *
from django.test.client import Client
from lettuce.django import django_url
from lxml import html
from splinter.browser import Browser
from nose.tools import assert_equals

urls = {'password passer': django_url('/passworder/')}

@before.all
def set_browser():
    world.browser = Browser('phantomjs')

@after.all
def teardown(total):
    world.browser.quit()


@step(r'I browse to the "([^"]*)" page')
def access_url(step, page_name):
    response = world.browser.visit(urls[page_name])