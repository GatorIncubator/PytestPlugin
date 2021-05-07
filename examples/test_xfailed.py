import pytest

# changed test_xfailed and replaced it with test_xdeclined. Then went into test_plugin_md.py and changed it to test_xdeclined on line 34.

@pytest.mark.xfail()
def test_xdeclined():
    assert False


class Test:
    @pytest.mark.xfail()
    def test_proceed(self):
        assert False
