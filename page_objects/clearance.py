"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class ClearancePage(Page):
    """ Class contains elements from Clearance page """
    def __init__(self, driver):
        super(ClearancePage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    good_look_text_button_android = (MobileBy.XPATH, '//android.widget.TextView[@text="Gold Look Heart Studs"]')

    # iOS
    good_look_text_button_ios = (MobileBy.XPATH, '//android.widget.TextView[@text="Gold Look Heart Studs"]')

    def navigate_to_good_look_element(self):
        self.swipe_to_element_visible(*getattr(self, 'good_look_text_button_' + self.os), x1=538, y1=1301, x2=538, y2=403, wait_time=350)

    def click_good_look_element_button(self):
        el = self.wait_for_element_present(*getattr(self, 'good_look_text_button_' + self.os))
        el.click()
