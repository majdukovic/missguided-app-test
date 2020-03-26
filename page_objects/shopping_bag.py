"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium.webdriver.common.mobileby import MobileBy

from page_objects.page import Page


class ShoppingBagPage(Page):
    """ Class contains elements from Header """
    def __init__(self, driver):
        super(ShoppingBagPage, self).__init__(driver)
        self.os = str(self.driver.desired_capabilities['platformName']).lower()

    # Android
    checkout_button_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/activity_modular_bag_checkout_button')
    title_text_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_title_text_view')
    product_size_and_color_text_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_size_color_text_view')
    total_price_text_android = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_subtotal_text_view')

    # iOS
    checkout_button_ios = (
    MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/activity_modular_bag_checkout_button')
    title_text_ios = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_title_text_view')
    product_size_and_color_text_ios = (
    MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_size_color_text_view')
    total_price_text_ios = (MobileBy.ID, 'com.poqstudio.app.platform.missguided:id/bag_item_subtotal_text_view')

    def get_product_title(self):
        """
        Get product title text
        :return: string - product title
        """
        product_title = self.get_element_text(*getattr(self, 'title_text_' + self.os))
        return product_title

    def get_product_size_and_color(self):
        """
        Get product size and color text
        :return: string - product size and color
        """
        product_size_and_color = self.get_element_text(*getattr(self, 'product_size_and_color_text_' + self.os))
        return product_size_and_color

    def click_checkout_button(self):
        """
        Click on checkout button
        :return: None
        """
        el = self.wait_for_element_present(*getattr(self, 'checkout_button_' + self.os))
        el.click()
