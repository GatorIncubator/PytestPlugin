import pytest


@pytest.mark.xfail()
def test_xproceed():
    assert True


class Test:
    @pytest.mark.xfail()
    def test_xproceed(self):
        assert True
