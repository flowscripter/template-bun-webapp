from behave import when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

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

    log.debug('waiting for element "{}" to have text "{}"'.format(element_id, message))

    def element_has_text(driver):
        value = driver.find_element(By.ID, element_id).get_property('value') or ''
        return message in value

    try:
        WebDriverWait(context.browser, 10).until(element_has_text)
    except TimeoutException:
        text = context.browser.find_element(By.ID, element_id).get_property('value')
        raise AssertionError(
            'expected "{}" to contain "{}", actual text was "{}"'.format(element_id, message, text))
