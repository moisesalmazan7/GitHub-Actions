from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(21, 5) == 1
        assert resto(8, 2) == 0
