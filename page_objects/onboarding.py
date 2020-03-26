"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class OnboardingPage(Page):
    """ Class contains elements for on-boarding page """
    def __init__(self, driver):
        super(OnboardingPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    get_started_button_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/onboarding_activity_get_started_btn')

    # iOS
    get_started_button_ios = (MobileBy.ACCESSIBILITY_ID, 'com.poqstudio.app.platform.missguided:id/onboarding_activity_get_started_btn')
    
    def click_get_started_button(self):
        """
        Click on Get Started button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'get_started_button_' + self.os))
        el.click()
