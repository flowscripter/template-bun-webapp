class element_value_is_non_empty(object):
    """An expectation for checking that an element has a text value which is not empty.

    locator - used to find the element
    returns the WebElement once it has a non empty value
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if len(element.get_property('value')) > 0:
            return element
        else:
            return False
