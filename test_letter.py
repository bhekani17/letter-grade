import unittest
from letter import letter_grade

class TestLetterGrade(unittest.TestCase):
    def test_a_grade(self):
        self.assertEqual(letter_grade(80), "A")
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(100), "A")

    def test_b_grade(self):
        self.assertEqual(letter_grade(70), "B")
        self.assertEqual(letter_grade(75), "B")
        self.assertEqual(letter_grade(79), "B")

    def test_c_grade(self):
        self.assertEqual(letter_grade(60), "C")
        self.assertEqual(letter_grade(65), "C")
        self.assertEqual(letter_grade(69), "C")

    def test_d_grade(self):
        self.assertEqual(letter_grade(50), "D")
        self.assertEqual(letter_grade(55), "D")
        self.assertEqual(letter_grade(59), "D")

    def test_f_grade(self):
        self.assertEqual(letter_grade(0), "F")
        self.assertEqual(letter_grade(40), "F")
        self.assertEqual(letter_grade(49), "F")

    def test_invalid_mark(self):
        with self.assertRaises(ValueError):
            letter_grade(-1)
        with self.assertRaises(ValueError):
            letter_grade(101)