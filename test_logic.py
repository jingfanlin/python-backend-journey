import pytest
from logic import get_status_info, InvalidStatusError, StatusNotFoundError


def test_valid_status():
    result = get_status_info("tired")
    assert result["msg"]


def test_status_not_found():
    with pytest.raises(StatusNotFoundError):
        get_status_info("ghost")


def test_invalid_status():
    with pytest.raises(InvalidStatusError):
        get_status_info("232421")