from pages.google.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()
        assert self.is_title, "Title is not Google."

    def search_text(self, text):
        element = self.get_search
        self.enter_text(element, text=text)

    def accept_cookies(self):
        element = self.get_accept_cookies_button()
        element.click()

    def open_result(self, text):
        expected_result = None
        results = self.get_all_result
        for result in results:
            if result.text == text:
                result.click()
                expected_result = result
                break
        assert expected_result is not None, 'Result not found on Google.'