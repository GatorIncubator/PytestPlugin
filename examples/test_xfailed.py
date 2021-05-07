import pytest


@pytest.mark.xfail()
def test_xdeclined():
    assert False


class Test:
    @pytest.mark.xfail()
    def test_proceed(self):
        assert False
