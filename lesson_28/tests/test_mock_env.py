import os
from unittest import mock

from logic.mock_env import get_app_name


@mock.patch.dict(
    os.environ, {"APP_NAME": "new-test-value"}
)
def test_get_app_name():
    assert "new-test-value" == get_app_name()
