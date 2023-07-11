from seasons import check_date
import pytest
from datetime import date


def test_bdate():
    assert check_date("2019-01-01") == date.fromisoformat("2019-01-01")
    with pytest.raises(SystemExit):
        assert check_date("1")
        assert check_date(1)