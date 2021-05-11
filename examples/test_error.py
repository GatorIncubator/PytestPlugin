def test_incorrect(invalid_fixture):
    pass


class Test:
    def test_incorrect(self, invalid_fixture):
        assert True

# changed test_error and replaced it with test_incorrect. Then went into test_plugin_md.py and changed test_error to test_incorrect on line 31.
