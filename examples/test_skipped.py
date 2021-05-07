import pytest

# changed test_skipped and replaced it with test_overlooked. Then went into test_plugin_md.py and changed test_skipped to test_overlooked on line 18, 29, 93, and 100.

def test_overlooked():
    pytest.skip()


class Test:
    def test_overlooked(self):
        pytest.skip()
