from logic.decorator import calculate


def test_calculate():
    assert calculate(2, 3) == 100
