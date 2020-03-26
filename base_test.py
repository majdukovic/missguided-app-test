# -*- coding: utf-8 -*-
"""
Created on March 26, 2020

@author: Mate Ajdukovic
"""

from appium import webdriver


class BaseTest:
    """
    This class deals with starting Appium server and Missguided app to the initial state
    All tests classes extend this class
    """
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '10.0',
        'automationName': 'uiautomator2',
        'deviceName': 'Android Emulator',
        'avd': 'Pixel_3',
        'autoGrantPermissions': True,
        'appPackage': 'com.poqstudio.app.platform.missguided',
        'appActivity': 'com.poqstudio.app.client.view.splash.MissguidedSplashActivity'
    }

    def setup(self):
        """
        Create driver instance with desired capabilities which will be used through tests suite
        """
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=self.desired_caps)

    def teardown(self):
        """
        Quit driver session and close app
        """
        self.driver.quit()
