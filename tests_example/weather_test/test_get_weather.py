import json
import unittest
from typing import Callable, Dict
from unittest.mock import patch, MagicMock

from tests_example.weather_test.get_weather import (
    get_weather,
    WEATHER_API_KEY,
    OPENWEATHER_API_URL,
    COLD,
    NORMAL,
    WARM,
    HOT
)


class TestGettingWeather(unittest.TestCase):
    api_key: str = None
    get_weather: Callable = None
    weather_api_url: str = None
    weather_conditions: Dict[str, str]
    json_test_file: str = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_key = WEATHER_API_KEY
        cls.weather_api_url = OPENWEATHER_API_URL
        cls.json_test_file = 'openweathermap_test_response.json'
        cls.weather_conditions = {
            'cold': COLD,
            'normal': NORMAL,
            'warm': WARM,
            'hot': HOT,
        }

    @patch('tests_example.weather_test.get_weather.requests')  # 'weather_test.get_weather.requests'
    def test_hot_weather_condition(self, requests_mock):
        with open(self.json_test_file) as file:
            body = json.load(file)
            print(f'\n ======= >>>> {body}')

        requests_response_mock = MagicMock()
        requests_response_mock.status_code = 200
        requests_response_mock.json.return_value = body
        requests_mock.get.return_value = requests_response_mock

        self.assertEqual(
            self.weather_conditions['hot'],
            get_weather(self.weather_api_url, self.api_key, 'Barcelona')
        )

    @patch('tests_example.weather_test.get_weather.requests')  # 'weather_test.get_weather.requests'
    def test_normal_weather_condition(self, requests_mock):
        requests_response_mock = MagicMock()
        requests_response_mock.status_code = 200
        requests_response_mock.json.return_value = {'main': {'temp': 15.3}}
        requests_mock.get.return_value = requests_response_mock

        self.assertEqual(
            self.weather_conditions['normal'],
            get_weather(self.weather_api_url, self.api_key, 'Barcelona')
        )

    @patch('tests_example.weather_test.get_weather.requests')  # 'weather_test.get_weather.requests'
    def test_api_error_with_incorrect_city(self, requests_mock):
        code = 404
        message = {'message': 'City not found'}

        requests_response_mock = MagicMock()
        requests_response_mock.status_code = code
        requests_response_mock.json.return_value = message
        requests_mock.get.return_value = requests_response_mock

        with self.assertRaises(RuntimeError) as error_context:
            get_weather(self.weather_api_url, self.api_key, 'Barcelona!!!')

        self.assertEqual(
            f'openweathermap.org returned non-200 code. Actual code is {code}, message is: {message["message"]}',
            str(error_context.exception)
        )
