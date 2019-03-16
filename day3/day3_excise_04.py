import unittest

def setUpModoule():
    print("*** setUpModule ***")

def tearDownModoule():
    print("*** tearDownModule ***")

class TestDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=== setUpClass1 ===")

    @classmethod
    def tearDownClass(cls):
        print("=== tearDownClass1 ===")
    def setup(self):
        print("--- setup ---")
    def tearDown(self):
        print("--- tearDown ---")
    def test_b(self):
        print("test_b")

    def test_a(self):
        print("test_a")

    def test_A(self):
        print("test_A")

class TestDemo2(unittest.TestCase):
    def test_c(self):
        print("test_c")




if __name__ == "__main__":
    unittest.main()