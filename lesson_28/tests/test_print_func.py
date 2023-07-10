from unittest import mock

from logic.print_func import print_datetime
from freezegun import freeze_time


@freeze_time("2023-07-10")
@mock.patch("logic.print_func.print")
def test_print_datetime(print_mock):
    print_datetime()
    print_mock.assert_called_with("2023-07-10 03:00:00")

