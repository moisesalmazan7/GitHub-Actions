from app.rot13_cipher import rot13 

class TestClass:
    def test_rot13(self):
        assert rot13("Me llamo Moisés") == "Zr yynzb Zbvféf"
        assert rot13("Tengo 23 años") == "Gratb 23 nñbf"    
