from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(5, 5) == 0
        assert resta(2, 1) == 1
        assert resta(7, 5) == 2
        assert resta(15, 9) == 6
