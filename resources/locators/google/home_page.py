from selenium.webdriver.common.by import By

class HomePageLocators():
    search_field = (By.NAME, "q")
    accept_cookies_button = (By.ID, "L2AGLb")
    first_result = (By.TAG_NAME, 'h3')

