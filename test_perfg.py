import unittest

from perfg import triangle, rectungle, circle

class FiguresTestCase(unittest.TestCase):

    def test_triangle_normal(self):
        res = triangle(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_zero(self):
        res = triangle(0, 5, 5)
        self.assertEqual(res, 10)

    def test_rectungle_normal(self):
        res = rectungle(10, 5)
        self.assertEqual(res, 30)

    def test_rectungle_square(self):
        res = rectungle(10, 10)
        self.assertEqual(res, 40)

    def test_circle_normal(self):
        res = circle(10)
        self.assertAlmostEqual(res, 62.8, places=2)

    def test_circle_zero(self):
        res = circle(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()