# -*- coding: utf-8 -*-
"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    StaleElementReferenceException, InvalidElementStateException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    """
    This class contains methods for checking if element is displayed, getting element text, etc.
    All page classes extend this class
    """
    def __init__(self, driver):
        """
            Constructor
        """
        self.driver = driver

    def is_element_visible(self, *locator, wait_time=15):
        """
        Check if element is visible and return result
        :param locator: Locator that needs to be found
        :param wait_time: Time to wait for the element. 15 seconds by default
        :return: True if element is found else False
        :rtype: boolean
        """
        try:
            WebDriverWait(self.driver, wait_time).until(lambda s: self.driver.find_element(*locator), message=":".join(locator) + " element not visible")
            return True
        except TimeoutException:
            return False

    def get_element_text(self, *locator, wait_time=15, value=False):
        """
        Get element text
        :param locator: Locator that needs to be found
        :param wait_time: Time to wait for the element. 15 seconds by default
        :return: Element text if element is found else pass
        :rtype: string
        """
        if str(self.driver.desired_capabilities['platformName']).lower() == 'android':
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(locator), message=":".join(locator) + " element not visible")
            return self.driver.find_element(*locator).get_attribute('text')
        else:
            WebDriverWait(self.driver, wait_time).until(lambda s: self.driver.find_element(*locator), message=":".join(locator) + " element not visible")
            if value:
                return self.driver.find_element(*locator).get_attribute('value')
            else:
                return self.driver.find_element(*locator).get_attribute('name')

    def wait_for_element_present(self, *locator, wait_time=10):
        """
        Wait 15 seconds for element to be displayed
        :param locator: Locator that needs to be found
        :param wait_time: Time to wait for the element. 15 seconds by default
        :return: None
        """
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        el = WebDriverWait(driver=self.driver, timeout=wait_time, ignored_exceptions=ignored_exceptions).until(lambda s: self.driver.find_element(*locator), message=":".join(locator) + " element not visible")
        return el

    def wait_for_elements_present(self, *locator, wait_time=15):
        """
        Wait 15 seconds for elements to be displayed
        :param locator: Locator that needs to be found
        :param wait_time: Time to wait for the element. 15 seconds by default
        :return: None
        """
        elements = WebDriverWait(self.driver, wait_time).until(lambda s: self.driver.find_elements(*locator), message=":".join(locator) + " elements not visible")
        return elements

    def swipe_to_element_visible(self, *locator, x1, y1, x2, y2, wait_time):
        """
        Swipe given coordinates, try to swipe for 5 total attempts
        :param x1: int - x1 coordinate
        :param y1: int - y1 coordinate
        :param x2: int - x2 coordinate
        :param y2: int - y2 coordinate
        :param locator: dict - element locator
        :return: None
        """
        # el_visible = False
        # count = 0
        # while el_visible is not True and count < 5:
        #     self.driver.swipe(x1, y1, x2, y2)
        #     el_visible = self.is_element_visible(locator, wait_time=2)
        #     count += 1

        el_visible = False
        count = 0
        while el_visible is not True and count < 5:
            try:
                action = TouchAction(self.driver)
                action \
                    .press(x=x1, y=y1) \
                    .wait(ms=wait_time) \
                    .move_to(x=x2, y=y2) \
                    .release()
                action.perform()
                el_visible = self.is_element_visible(*locator, wait_time=2)
            except InvalidElementStateException:
                pass
            count += 1
