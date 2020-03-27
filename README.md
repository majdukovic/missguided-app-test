# missguided-app-test

This repository contains
 - test for adding product to the bag for Missguided app using Appium and Android
 - tests for Login/Logout/Registration/Viewing product details with Postman

Steps to execute test with Android and Appium:
1. Setup Appium
2. Install PyCharm
3. Install Python 3.6.8
4. Create and activate virtualenv 
5. Install required packages (run: pip install -r requirements.txt)
6. Create Android emulator as per "desired_caps" from BaseTest class or set "desired_caps" for real device
7. Install Missguided app from Play store
7. Run tests from project root directory with command: nosetests -s --tc-format=python tests.test_add_items

Video of test run: https://youtu.be/oSIurGd0GvI

Steps to execute tests with Postman:
1. Install Postman
2. Import Postman collection from "postman_tests" directory
3. Click Send request
4. View results from "Test Results" tab

![](https://media.giphy.com/media/VDMF41fANZEeYztoCj/giphy.gif)
