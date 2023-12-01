import unittest

from adv001.main import get_calibration_value, calc_line


class TestFunction(unittest.TestCase):

    def test_get_cal_values(self):
        cases = [
            ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"],
            ["gfhctvvksix855qz1", "six5twovfdpcjpbgntzkp9four", "3seven4five9"]
        ]

        results = [
            142, 179
        ]

        for i, case in enumerate(cases):
            self.assertEqual(results[i], get_calibration_value(case))

    def test_calc_word(self):
        cases = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f"
            "treb7uchet"
        ]

        results = [
            12, 38, 15, 77
        ]

        for i, case in enumerate(cases):
            self.assertEqual(results[i], calc_line(case))

    def test_calc_word_2(self):
        cases = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

        results = [
            29,
            83,
            13,
            24,
            42,
            14,
            76
        ]

        for i, case in enumerate(cases):
            self.assertEqual(results[i], calc_line(case))
