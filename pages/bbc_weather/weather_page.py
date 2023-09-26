from pages.bbc_weather.base_page import BasePage
class WeatherPage(BasePage):
    def __init__(self, driver, city:str):
        self.city = city
        super().__init__(driver=driver)


    def validate(self):
        assert self.is_title(title=f"{self.city} - BBC Weather"), f"{self.city} - BBC Weather doesn't appear as Title."
        assert self.get_location.text == self.city.capitalize(), f"{self.city} not found as selected location."
        self.validate_today_square()

    def validate_today_square(self):
        """Validate the today square data."""
        scroll = self.driver.find_element(*self.locators_weather.days_scroll)
        square = scroll.find_element(*self.locators_weather.today_square)
        today = square.find_element(*self.locators_weather.today_label)
        assert today.text in ['Today', 'Tonight'], "'Today' not found."

        """Get Higher temperature of today"""
        high_temperature = square.find_element(*self.locators_weather.today_high_temperature)
        high_temperature_value = high_temperature.find_element(*self.locators_weather.temperature_value_label)

        """Validate celsius symbol"""
        assert 'º' in high_temperature_value, "Symbol 'º' not found in the lower temperature."
        """Remove symbol from temperature"""
        high_temperature_value = high_temperature_value.replace('°', ' ')
        assert isinstance(int(high_temperature_value.text),int), "High temperature not found"

        """Get Lower temperature of today"""
        low_temperature = square.find_element(*self.locators_weather.today_low_temperature)
        low_temperature_value = low_temperature.find_element(*self.locators_weather.temperature_value_label).text
        print(low_temperature_value)
        print(bool("º" in low_temperature_value))

        """Validate celsius symbol"""
        assert bool("º" in low_temperature_value), "Symbol 'º' not found in the lower temperature."
        """Remove symbol from temperature"""
        low_temperature_value = low_temperature_value.replace('°', ' ')
        """Validate temperature"""
        assert isinstance(int(low_temperature_value),int), "Lower temperature not found"
