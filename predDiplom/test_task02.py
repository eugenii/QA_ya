import pytest


SUPPORTED_TIMEZONES = ['UTC', 'Europe/Moscow', 'Asia/Tokyo', 'America/New_York']
TEST_ZONES = ['UTC', 'Europe/London', 'Asia/Tokyo', 'Pacific/Auckland']

# напиши функцию is_timezone_supported для проверки поддерживаемых зон


# добавь тест test_timezone_support с параметризацией для проверки этих зон:
# 'UTC', 'Europe/London', 'Asia/Tokyo', 'Pacific/Auckland', 'Africa/Cairo'

def is_timezone_supported(timezone):
    return timezone in SUPPORTED_TIMEZONES


@pytest.mark.parametrize('timezone, result', [
                         [TEST_ZONES[0], True],
                         [TEST_ZONES[1], False],
                         [TEST_ZONES[2], True],
                         [TEST_ZONES[3], False],
                         [TEST_ZONES[4], False]]
                         )
def test_timezone_support(timezone, result):

    assert is_timezone_supported(timezone) == result
