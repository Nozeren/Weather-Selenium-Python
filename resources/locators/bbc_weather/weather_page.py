from selenium.webdriver.common.by import By

class WeatherLocators():
    location_label = (By.ID, 'wr-location-name-id')
    days_scroll = (By.CLASS_NAME, 'wr-day-carousel')
    today_square = (By.ID, 'daylink-0')
    today_label = (By.XPATH, "//div[@class='wr-day__title wr-js-day-content-title']")
    today_high_temperature = (By.CLASS_NAME, 'wr-day-temperature__high-value')
    today_low_temperature = (By.CLASS_NAME, 'wr-day-temperature__low-value')
    temperature_value_label = (By.CLASS_NAME, 'wr-value--temperature--c')
