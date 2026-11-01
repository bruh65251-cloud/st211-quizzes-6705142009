from unittest.mock import patch
from weather import describe_weather

def test_hot_weather():
    with patch('weather.get_temperature', return_value=30):
        result = describe_weather()
        assert result == "Hot"

def test_freezing_weather():
    with patch('weather.get_temperature', return_value=-5):
        result = describe_weather()
        assert result == "Freezing"

"""wanna know how things work behind the scenes? 
and specify the return value to see how we can use mock to test our code without relying on random values or external dependencies."""