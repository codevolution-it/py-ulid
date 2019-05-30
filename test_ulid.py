# content of test_ulid.py

import ulid
import pytest


class TestUlid(object):
    def test_generate_length(self):
        _ulid = ulid.ULID()
        val = _ulid.generate()
        print(val)
        assert len(val) == 26

    def test_ulid_max(self):
        with pytest.raises(ValueError, match=r".*128-bit.*"):
            ulid.ULID(340282366920938463463374607431768211459)

    def test_ulid_min(self):
        with pytest.raises(ValueError, match=r".*128-bit.*"):
            ulid.ULID(-1)
