from resources.locators.bbc_weather.home_page import HomePageLocators
from resources.locators.bbc_weather.weather_page import WeatherLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators_home = HomePageLocators()
        self.locators_weather = WeatherLocators()
        self.wait = WebDriverWait(driver, 10)

    def is_title(self, title):
        return self.driver.title == title

    def get_search(self):
        element = self.driver.find_element(*self.locators_home.search_field)
        return element

    @staticmethod
    def enter_text(element, text: str):
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
        return element

    def get_accept_cookies_button(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.locators_home.cookies_frame))
        return self.wait.until(EC.element_to_be_clickable(self.locators_home.cookies_accept_button))

    def select_correct_country(self, element, country: str, city: str):
        options = element.find_elements(*self.locators_home.country_selector)
        result = None
        expected_result = city + ", " + country
        for option in options:
            if option.text == expected_result:
                result = option.text
                option.click()
                break
        assert result == expected_result, "Country not found"
    @property
    def get_location(self):
        return self.driver.find_element(*self.locators_weather.location_label)
