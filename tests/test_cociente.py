from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(10, 5) == 2
        assert cociente(20, 4) == 5
        assert cociente(10, 1) == 10
        assert cociente(18, 9) == 2
