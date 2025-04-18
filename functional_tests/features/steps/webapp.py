from behave import when, then
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from helper.selenium import element_value_is_non_empty

import logging

log = logging.getLogger("webapp")


@when('the webapp URL "{page}" is loaded')
def step_impl(context, page):
    url = "http://{}:{}/{}".format(context.address, context.port, page)
    context.browser.get(url)


@when('the page element with ID "{element_id}" is available')
def step_impl(context, element_id):
    log.debug('waiting for element "{}"'.format(element_id))

    WebDriverWait(context.browser, 3).until(presence_of_element_located((By.ID, element_id)))


@then('the page element with ID "{element_id}" should have text "{message}"')
def step_impl(context, element_id, message):

    log.debug('waiting for element "{}" to have a text value'.format(element_id))

    WebDriverWait(context.browser, 3).until(element_value_is_non_empty((By.ID, element_id)))

    text = context.browser.find_element(By.ID, element_id).get_property('value')

    log.debug('looking for "{}" in "{}"'.format(message, text))

    assert message in text
