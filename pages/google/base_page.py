from resources.locators.google.home_page import HomePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = HomePageLocators()
        self.wait = WebDriverWait(driver, 10)

    @property
    def get_search(self):
        element = self.driver.find_element(*self.locators.search_field)
        return element

    def get_accept_cookies_button(self):
        return self.driver.find_element(*self.locators.accept_cookies_button)

    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    @property
    def is_title(self) -> str:
        return self.driver.title == "Google"

    @property
    def get_all_result(self):
        self.wait.until(EC.presence_of_element_located(self.locators.first_result))
        return self.driver.find_elements(*self.locators.first_result)