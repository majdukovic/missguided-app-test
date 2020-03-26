"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class HeaderPage(Page):
    """ Class contains elements from Header """
    def __init__(self, driver):
        super(HeaderPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    more_info_button_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/action_more')
    menu_button_android = (MobileBy.ACCESSIBILITY_ID, 'Open navigation drawer')
    clearance_button_android = (MobileBy.XPATH, '//android.widget.TextView[@text="Clearance"]')
    most_wanted_button_android = (MobileBy.XPATH, '//android.widget.TextView[@text="Most Wanted"]')
    sale_button_android = (MobileBy.XPATH, '//android.widget.TextView[@text="SALE"]')
    bag_button_android = (MobileBy.ACCESSIBILITY_ID, 'Bag')

    # iOS
    more_info_button_ios = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/action_more')
    menu_button_ios = (MobileBy.ACCESSIBILITY_ID, 'Open navigation drawer')
    clearance_button_ios = (MobileBy.XPATH, '//android.widget.TextView[@text="Clearance"]')
    most_wanted_button_ios = (MobileBy.XPATH, '//android.widget.TextView[@text="Most Wanted"]')
    sale_button_ios = (MobileBy.XPATH, '//android.widget.TextView[@text="SALE"]')
    bag_button_ios = (MobileBy.ACCESSIBILITY_ID, 'Bag')

    def click_more_info_button(self):
        el = self.wait_for_element_present(*getattr(self, 'more_info_button_' + self.os))
        el.click()

    def click_menu_button(self):
        el = self.wait_for_element_present(*getattr(self, 'menu_button_' + self.os))
        el.click()

    def navigate_to_clearance_section(self):
        self.wait_for_element_present(*getattr(self, 'sale_button_' + self.os))
        self.driver.swipe(start_x=377, start_y=1579, end_x=377, end_y=547)
        self.driver.swipe(start_x=320, start_y=1479, end_x=320, end_y=447)

    def click_clearance_button(self):
        el = self.wait_for_element_present(*getattr(self, 'clearance_button_' + self.os))
        el.click()

    def click_bag_button(self):
        el = self.wait_for_element_present(*getattr(self, 'bag_button_' + self.os))
        el.click()
