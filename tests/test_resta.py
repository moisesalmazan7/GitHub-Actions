from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(4, 5) == -1
        assert resta(2, 1) == 1
        assert resta(7, 5) == 2
        assert resta(7, 9) == -2
