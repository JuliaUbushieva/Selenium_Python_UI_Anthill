# #  method to create a Wiki-Space-Homepage object
# # contains all basic methods to run on this page
# # ! we should provide browser and URL of the page as parameters when creating an instance of that class
#
# from locators.wikispace_home_page_locators import WikiSpaceHomePageLocators
# from pages.base_page import BasePage
#
# class WikiSpaceHomePage(BasePage):
#
#     # checks that the space title shown matches to the title-to-compare provided
#     def title_shown_is_correct(self, title_to_compare_with):
#         title_element = self.browser.find_element(*WikiSpaceHomePageLocators.SPACE_TITLE)
#         if title_element.text == title_to_compare_with:
#             return True
#
#     def all_other_elements_of_page_present(self):
#         favorite_pages_area_label = self.browser.find_elements(*WikiSpaceHomePageLocators.FAVORITE_PAGES_AREA_LABEL)
#         all_pages_label = self.browser.find_elements(*WikiSpaceHomePageLocators.ALL_PAGES_LABEL)
#         default_page_for_space_field_label = self.browser.find_elements(
#             *WikiSpaceHomePageLocators.DEFAULT_PAGE_FOR_SPACE_FIELD_LABEL)
#         if (len(favorite_pages_area_label) == 1) and (len(all_pages_label) == 1) and len(
#                 default_page_for_space_field_label) == 1:
#             return True
#
#     def navigate_to_wiki(self):
#         wiki_button = self.browser.find_element(*WikiSpaceHomePageLocators.WIKI_BUTTON)
#         wiki_button.click()
