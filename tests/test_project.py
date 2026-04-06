from src.main import get_city,ask_user,get_important_data
import unittest

class TestWeatherApp(unittest.TestCase):
    def test_get_city(self):
        assert get_city("London", "UK") == "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/"
        assert get_city("New York", "US") == "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/New York,US/"
    def test_important_data(self):
        mock_api_response = {
                "days": [
                        {"datetime": "2026-04-06", "temp": 68, "humidity": 55, "description": "Sunny"},
                        {"datetime": "2026-04-07", "temp": 71, "humidity": 60, "description": "Cloudy"},
                    ]
                }
        important_data,days,temps=get_important_data(mock_api_response,1)
        assert important_data[0]["temperature in °C"] == 20  
        assert important_data[0]["humidity in %"] == 55