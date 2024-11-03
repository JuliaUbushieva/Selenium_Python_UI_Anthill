# # test scenario ID 1: create a new space on Wiki page, starts editing and save it (but no changes were made actually),
# # then go back to the Wiki page - and check that the space with the same title and description was created
# # and now is listed on the Wiki page
#
# from pages.wiki_page import WikiPage
# from pages.add_wikispace_page import WikiAddSpacePage
# from pages.edit_wikispace_page import WikiEditSpacePage
# from pages.dasboard_page import DashboardPage
# from config import Urls
# from tests.test_data import TestData
# import pytest
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from locators.edit_wikispace_page_locators import EditWikiSpacePageLocators
# from pages.wikispace_home_page import WikiSpaceHomePage
# import allure
# from allure_commons.types import AttachmentType
#
#
#
# class TestScenarioCreateWikiSpace:
#
#     @pytest.mark.smoke
#     @pytest.mark.regression
#     @pytest.mark.parametrize("space_data", TestData.space_data)
#     def test_create_and_edit_space(self, browser, space_data, admin_login):  # admin_login here is a fixture to log in first
#         dashboard_page = DashboardPage(browser, Urls.dashboard_page)
#         time.sleep(2)
#         dashboard_page.navigate_to_wiki()
#
#         wiki_page = WikiPage(browser, Urls.wiki_page)
#         wiki_page.navigate_to_create_space()
#         assert browser.current_url == Urls.wiki_add_space_page
#
#         wiki_add_space = WikiAddSpacePage(browser, Urls.wiki_add_space_page)
#         wiki_add_space.create_space(space_data)  # creates a space with test data provided
#
#         wiki_edit_page = WikiEditSpacePage(browser, Urls.wiki_edit_space_page)  # to start editing the space
#         wiki_edit_page.save_edit_space_result()  # and save results (actually, no changes were made)
#         #  and check that popup message about saving was showed
#         assert WebDriverWait(browser, 3).until(EC.presence_of_element_located(EditWikiSpacePageLocators.CHANGES_SAVED_POPUP)).text == "Успех"
#
#         #  check that the space created now is shown in the list of spaces on Wiki page
#         wiki_edit_page.navigate_to_spaces_list()
#         wiki_page = WikiPage(browser, Urls.wiki_page)
#         time.sleep(1)
#         assert wiki_page.space_with_some_title_listed(space_data["title"])
#         assert wiki_page.space_with_description_listed(space_data["desc"])
#
#         #  check that we can open the space created, and the space title inside matches
#         wiki_page.navigate_to_space_with_title(space_data["title"])
#         time.sleep(2)
#         wiki_space_home_page = WikiSpaceHomePage(browser, Urls.wiki_space_home_page)
#         assert wiki_space_home_page.title_shown_is_correct(space_data["title"])
#         assert wiki_space_home_page.all_other_elements_of_page_present()
#         time.sleep(2)
#
#         #  TODO: delete the test space created?
#         # wiki_space_home_page.navigate_to_wiki()
#         # time.sleep(1)
#         # wiki_page.delete_space_with_title(space_data["title"])
#
#
#
#
#
#
#
#
#
