from src.main import addition


def test_addition():
    result = addition(1, 3)
    assert result == 4
