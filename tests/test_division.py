from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(20, 5) == 4
        assert division(8, 2) == -4
        assert division(10, 5) == 2
        assert division(9, 9) == 1
