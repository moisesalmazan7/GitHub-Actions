from app.operaciones import suma

class TestClass:
    def test_suma(self):
        assert suma(6, 5) == 1
