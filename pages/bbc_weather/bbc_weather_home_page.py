from pages.bbc_weather.base_page import BasePage
import time


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.implicitly_wait(10)
        assert self.is_title(title="BBC Weather - Home"), "BBC Weather Home doesn't appear as Title."

    def search_city(self, country: str, city: str):
        element = self.get_search()
        element = self.enter_text(element, text=city)
        self.select_correct_country(element, country=country, city=city)

    def accept_cookies(self):
        element = self.get_accept_cookies_button()
        element.click()
        self.driver.switch_to.default_content()
