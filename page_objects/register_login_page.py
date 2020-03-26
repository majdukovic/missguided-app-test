"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class RegisterLoginPage(Page):
    """ Class contains elements from Header """
    def __init__(self, driver):
        super(RegisterLoginPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    sign_in_button_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/content_block_login_view_sign_in_button')

    # iOS
    sign_in_button_ios = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/content_block_login_view_sign_in_button')

    def is_displayed_sign_in_button(self):
        """
        Check if element is displayed
        :return: boolean - True if element is displayed, otherwise return False
        """
        sign_in_button_displayed = self.is_element_visible(*getattr(self, 'sign_in_button_' + self.os))
        return sign_in_button_displayed
