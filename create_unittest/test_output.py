import unittest
from test import multiply2

class TestMultiply2(unittest.TestCase):

    def test_multiply2_positive_number(self):
        self.assertEqual(multiply2(3), 6)

    def test_multiply2_zero(self):
        self.assertEqual(multiply2(0), 0)

    def test_multiply2_negative_number(self):
        self.assertEqual(multiply2(-3), -6)

    def test_multiply2_float_number(self):
        self.assertAlmostEqual(multiply2(2.5), 5.0)

    def test_multiply2_string(self):
        with self.assertRaises(TypeError):
            multiply2("hello")

    def test_multiply2_list(self):
        with self.assertRaises(TypeError):
            multiply2([1, 2])

    def test_multiply2_tuple(self):
        with self.assertRaises(TypeError):
            multiply2((1, 2))

    def test_multiply2_dict(self):
        with self.assertRaises(TypeError):
            multiply2({"key": "value"})

    def test_multiply2_set(self):
        with self.assertRaises(TypeError):
            multiply2({1, 2})

    def test_multiply2_none(self):
        self.assertIsNone(multiply2(None))

    def test_multiply2_large_number(self):
        self.assertEqual(multiply2(1000), 2000)

    def test_multiply2_small_number(self):
        self.assertEqual(multiply2(-5), -10)

    def test_multiply2_even_number(self):
        self.assertEqual(multiply2(4), 8)

    def test_multiply2_odd_number(self):
        self.assertEqual(multiply2(5), 10)

if __name__ == '__main__':
    unittest.main()