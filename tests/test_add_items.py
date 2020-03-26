# -*- coding: utf-8 -*-
"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from nose.tools import assert_true

from base_test import BaseTest
from page_objects.clearance import ClearancePage
from page_objects.header import HeaderPage
from page_objects.onboarding import OnboardingPage
from page_objects.product import ProductPage
from page_objects.register_login_page import RegisterLoginPage
from page_objects.shopping_bag import ShoppingBagPage


class TestAddItems(BaseTest):
    """
    Test suite deals with adding items to bag
    """

    def test_01_add_item_to_basket_and_select_pay(self):
        """
        Open Menu
        Click on Clearance section
        Select 7th item from Clearance section
        Add to bag
        Select Size
        Select the Bag
        Verify correct title, size and color is displayed
        Select Checkout
        Verify Sign In button is displayed
        """
        onboarding_page = OnboardingPage(self.driver)
        header_page = HeaderPage(self.driver)
        clearance_page = ClearancePage(self.driver)
        product_page = ProductPage(self.driver)
        shopping_bag_page = ShoppingBagPage(self.driver)
        register_login_page = RegisterLoginPage(self.driver)

        onboarding_page.click_get_started_button()
        header_page.click_menu_button()
        header_page.navigate_to_clearance_section()
        header_page.click_clearance_button()
        clearance_page.navigate_to_good_look_element()
        clearance_page.click_good_look_element_button()
        product_page.navigate_to_add_to_bag_button()
        product_page.click_add_to_bag_button()
        product_page.select_size(size='one')
        header_page.click_bag_button()
        product_title = shopping_bag_page.get_product_title()
        assert_true(product_title == 'Gold Look Heart Studs', msg="Incorrect product title displayed.")
        product_size_and_color = shopping_bag_page.get_product_size_and_color()
        assert_true(product_size_and_color == 'ONE Gold', msg="Incorrect size and color displayed.")
        shopping_bag_page.click_checkout_button()
        assert_true(register_login_page.is_displayed_sign_in_button(), msg="Sign in button is not displayed.")
        print("Sign in button is displayed.")
