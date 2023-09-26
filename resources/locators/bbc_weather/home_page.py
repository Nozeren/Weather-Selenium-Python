from selenium.webdriver.common.by import By

class HomePageLocators():
    search_field = (By.ID, "ls-c-search__input-label")
    country_selector = (By.XPATH, "//a[@class='ls-o-location ls-o-location--dark gel-pica']")

    # Cookies
    cookies_frame = (By.XPATH, '//*[@id="sp_message_iframe_783538"]')
    cookies_accept_button = (By.XPATH, "//button[contains(text(),'I agree')]")