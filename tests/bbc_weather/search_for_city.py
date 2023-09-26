import unittest
from pages.google import google_home_page
from pages.bbc_weather import bbc_weather_home_page, weather_page
from tests.base_test import BaseTest

class SearchForCity(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        # Open Google
        self.google_home_page = google_home_page.HomePage(driver=self.driver)

    def test_Search_For_City(self):
        # Accept Google Cookies
        self.google_home_page.accept_cookies()
        # Search for BBC Weather & Open Website
        self.google_home_page.search_text(text="BBC Weather")
        self.google_home_page.open_result(text="BBC Weather - Home")
        self.bbc_weather_home_page = bbc_weather_home_page.HomePage(driver=self.driver)
        # Accept BBC Cookies
        self.bbc_weather_home_page.accept_cookies()
        # Search/select a city
        self.bbc_weather_home_page.search_city(country="Greece",city="Athens")
        self.weather = weather_page.WeatherPage(driver=self.driver, city="Athens")
        self.weather.validate()

if __name__ == "__main__":
    unittest.main()