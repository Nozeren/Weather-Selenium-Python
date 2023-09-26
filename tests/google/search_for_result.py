import unittest
from pages.google import google_home_page
from tests.base_test import BaseTest

class SearchForResult(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        # Open Google
        self.google_home_page = google_home_page.HomePage(driver=self.driver)

    def test_Search_For_Result(self):
        # Accept Google Cookies
        self.google_home_page.accept_cookies()
        # Search for BBC Weather & Open Website
        self.google_home_page.search_text(text="Github")
        self.google_home_page.open_result(text="GitHub: Let's build from here · GitHub")

if __name__ == "__main__":
    unittest.main()