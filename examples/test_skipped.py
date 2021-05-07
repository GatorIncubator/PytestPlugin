import pytest


def test_overlooked():
    pytest.skip()


class Test:
    def test_overlooked(self):
        pytest.skip()
