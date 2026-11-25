import unittest
from plosfg import triangle, rectangle, circle

class FiguresTestCase(unittest.TestCase):

    def test_triangle_normal(self):
        res = triangle(10, 5)
        self.assertEqual(res, 25)

    def test_triangle_zero(self):
        res = triangle(0, 5)
        self.assertEqual(res, 0)

    def test_rectangle_normal(self):
        res = rectangle(10, 5)
        self.assertEqual(res, 50)

    def test_rectangle_square(self):
        res = rectangle(10, 10)
        self.assertEqual(res, 100)

    def test_circle_normal(self):
        res = circle(10)
        self.assertAlmostEqual(res, 314.0, places=1)

    def test_circle_zero(self):
        res = circle(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()