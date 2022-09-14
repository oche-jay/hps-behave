import pytest
from pytest_bdd import given, when, then
from playwright.sync_api import Page

from features.steps.actionwords import Actionwords


class MyContext:
    def __init__(self, page):
        self.actionwords = Actionwords(page)
        self.page = page
    pass


@pytest.fixture
def my_context(page: Page):
    return MyContext(page)


@given("I am a registered user")
def step_impl(my_context):
    region = "us4"
    user = f"sre+synthetics-{region}@salesloft.com"
    password = ''

    my_context.actionwords.set_user_details(user, password)


@when("I login to Salesloft")
def step_impl(my_context):
    my_context.actionwords.i_login_to_salesloft()


@when("I create a new person")
def step_impl(my_context):
    my_context.actionwords.create_a_new_person()


@then("the person should be in the database")
def step_impl(my_context):
    pass


@when('I login to Salesloft in "us3"')
def step_impl():
    raise NotImplementedError(u'STEP: When I login to Salesloft in "us3"')


@given("I navigate to Cadence")
def step_impl():
    raise NotImplementedError(u'STEP: And I navigate to Cadence')


@given("I place a phone call to test number")
def step_impl():
    raise NotImplementedError(u'STEP: And I place a phone call to test number')


@then("it should connect to a keyscore router")
def step_impl():
    raise NotImplementedError(u'STEP: Then it should connect to a keyscore router')


@given("some events should show up in Kafka")
def step_impl():
    raise NotImplementedError(u'STEP: And some events should show up in Kafka')