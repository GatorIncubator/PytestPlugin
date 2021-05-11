import pytest

# changed test_xpassed and replaced it with test_xproceed. Then went into test_plugin_md.py and changed test_error to text_xproceed on line 37.

@pytest.mark.xfail()
def test_xproceed():
    assert True


class Test:
    @pytest.mark.xfail()
    def test_xproceed(self):
        assert True
