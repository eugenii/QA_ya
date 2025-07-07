from unittest.mock import MagicMock, Mock


def should_open_windows(weather_data):
    if weather_data.get('rain') or (weather_data.get('temperature', 0) < 10):
        return False
    return True


class TestShouldOpenWindows:
    def test_ideal_conditions(self):
        # mock_weather_service = MagicMock()
        # mock_weather_service.get.side_effect = lambda key, default=None: {
        #     'rain': False,
        #     'temperature': 20
        # }.get(key, default)
        mock_weather_service = Mock()
        mock_weather_service.get.return_value = {'rain': False, 'temperature': 20}
        assert should_open_windows(mock_weather_service) == False

    def test_cold_weather(self):
        # mock_weather_service = MagicMock()
        # mock_weather_service.get.side_effect = lambda key, default=None: {
        #     'rain': False,
        #     'temperature': 5
        # }.get(key, default)
        mock_weather_service = Mock()
        mock_weather_service.get.return_value = {'rain': False, 'temperature': 5}
        assert should_open_windows(mock_weather_service) == False

    def test_rainy_weather(self):
        # mock_weather_service = MagicMock()
        # mock_weather_service.get.side_effect = lambda key, default=None: {
        #     'rain': True,
        #     'temperature': 15
        # }.get(key, default)
        mock_weather_service = Mock()
        mock_weather_service.get.return_value = {'rain': True, 'temperature': 15}
        assert should_open_windows(mock_weather_service) == False