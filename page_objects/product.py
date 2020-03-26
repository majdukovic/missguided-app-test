"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class ProductPage(Page):
    """ Class contains elements from Product page """
    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    add_to_bag_button_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/product_info_section_add_to_bag_button')
    select_size_one_android = (MobileBy.XPATH, '//android.widget.TextView[@text="ONE"]')

    # iOS
    add_to_bag_button_ios = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/product_info_section_add_to_bag_button')
    select_size_one_ios = (MobileBy.XPATH, '//android.widget.TextView[@text="ONE"]')

    def navigate_to_add_to_bag_button(self):
        """
        Navigate to Add to bag element
        :return: None
        """
        self.swipe_to_element_visible(*getattr(self, 'add_to_bag_button_' + self.os), x1=538, y1=1301, x2=538,
                                      y2=403, wait_time=300)

    def click_add_to_bag_button(self):
        """
        Click on Add to bag element
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'add_to_bag_button_' + self.os))
        el.click()

    def select_size(self, size):
        """
        Click on Select size element
        :param size: string - text of the element size
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'select_size_' + size + '_' + self.os))
        el.click()
