def subract(a,b):
    return (a-b)
import unittest
class subtractclass(unittest.TestCase):
    def test1(self):
        result = subract(10,7)
        self.assertEqual(result,3)
    def test2(self):
        result = subract(0,3)
        self.assertEqual(result,-3)
    def test3(self):
        result = subract(3,-0)
        self.assertEqual(result,3)
    def test4(self):
        result = subract(-8,-8)
        self.assertEqual(result,0)
    def test5(self):
        result = subract(8,-7)
        self.assertEqual(result,15)
    def test6(self):
        result = subract(-8,-7)
        self.assertEqual(result,-1)
if __name__ == '__main__':
    unittest.main()
