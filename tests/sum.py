import unittest

def sum(a, b):
    try:
        return a + b
    except Exception:
        return None

class SumFunctionTest(unittest.TestCase):
    def test_sum(self):
        foo = sum(10, 10)
        
        self.assertEqual(foo, 20)
        self.assertIsNotNone(foo)


if __name__ == "__main__":
    unittest.main()