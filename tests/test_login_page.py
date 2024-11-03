#  file to collect tests created for login page
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from config import Urls
import time

# import allure
# from allure_commons.types import AttachmentType

load_dotenv()


class TestLoginPage:

    # @allure.feature('User login')
    # @allure.story('With valid credentials')
    # @allure.severity('blocker')
    # @pytest.mark.parametrize('email', TestData.valid_login_credentials_client)
    # @pytest.mark.smoke
    # @pytest.mark.regression
    def test_login(self, browser):
        login_page = LoginPage(browser, os.environ["BASE_LOGIN_URL"])
        login_page.open()
        login_page.enter_email(os.environ["VALID_LOGIN_CLIENT"])
        login_page.enter_password(os.environ["VALID_LOGIN_PASSWORD"])
        login_page.submit_login()
        time.sleep(2)
        # with allure.step('Making screenshot'):
        #     allure.attach(browser.get_screenshot_as_png(), name='result1', attachment_type=AttachmentType.PNG)
        assert browser.current_url == Urls.MAIL_URL, f"Wrong result, expected to be on Mail page"

    # @allure.feature('User login')
    # @allure.story('With invalid credentials')
    # @allure.severity('blocker')
    # @pytest.mark.parametrize("invalid_credentials", TestData.invalid_login_credentials_admin)
    # @pytest.mark.smoke
    # @pytest.mark.regression
    # def test_login_with_invalid(self, browser, invalid_credentials):
    #     login_page = LoginPage(browser, Links.login_page)
    #     login_page.open()
    #     login_page.login(invalid_credentials)
    #     # time.sleep(2)
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result2', attachment_type=AttachmentType.PNG)
    #     assert browser.current_url == Links.login_page, f"Wrong result, expected to stay on Login page"
    #     assert login_page.login_error_message_shown(), f"Wrong result, no error message shown"
    #
    # @allure.feature('Login page elements')
    # @allure.story('Check navigation elements')
    # @allure.severity('blocker')
    # @pytest.mark.smoke
    # @pytest.mark.regression
    # def test_navigation_elements(self, browser):
    #     login_page = LoginPage(browser, Links.login_page)
    #     login_page.open()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result3', attachment_type=AttachmentType.PNG)
    #
    #     assert login_page.forgot_password_link_exists()
    #     login_page.navigate_to_forgot_password()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result4', attachment_type=AttachmentType.PNG)
    #     assert browser.current_url == Links.forgot_password, f"Wrong result, expected to be on Forgot Password page"
    #     login_page.open()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result5', attachment_type=AttachmentType.PNG)
    #
    #
    #     assert login_page.remember_me_checkbox_exists(), f"Wrong result, no 'Remember me' checkbox found"
    #     login_page.check_remember_me()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result6', attachment_type=AttachmentType.PNG)
    #     assert login_page.remember_me_checked(), f"Wrong result, 'Remember me' is not checked"
    #     login_page.check_remember_me()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result7', attachment_type=AttachmentType.PNG)
    #     assert login_page.remember_me_unchecked(), f"Wrong result, 'Remember me' is still checked"
    #
    #     assert login_page.create_account_link_exists()
    #     login_page.navigate_to_create_account()
    #     time.sleep(2)
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result8', attachment_type=AttachmentType.PNG)
    #     assert browser.current_url == Links.register_page, f"Wrong result, expected to be on Create an account page"
    #     login_page.open()
    #     with allure.step('Making screenshot'):
    #         allure.attach(browser.get_screenshot_as_png(), name='result9', attachment_type=AttachmentType.PNG)
    #
    #     #  AFTER DEVELOPING FUNCTIONALITY TO LOG IN WITH GOOGLE, FACEBOOK OR TWITTER ACCOUNT
    #     # this test could be updated with assertions
    #     # for page redirection after clicking on these buttons
    #     assert login_page.login_with_facebook_exists(), f"Wrong result, no button to log in with Facebook account found"
    #     assert login_page.login_with_google_exists(), f"Wrong result, no button to log in with Google account found"
    #     assert login_page.login_with_twitter_exists(), f"Wrong result, no button to log in with Twitter account found"
