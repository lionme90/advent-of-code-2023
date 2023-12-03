import unittest

from main import find_adjusted, find_adjusted_with_gears


class TestFunction(unittest.TestCase):

    def test_find_all_adjusted_weird_new_line(self):
        scheme = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*.....*",
            "*....+.588",
            "8.592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

        result = find_adjusted(scheme)
        print(result)
        self.assertEqual(4957, sum(result))

    def test_find_all_adjusted(self):
        scheme = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

        result = find_adjusted(scheme)
        print(result)
        self.assertEqual(4361, sum(result))

    def test_find_gears(self):
        scheme = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]

        result = find_adjusted_with_gears(scheme)
        print(result)
        self.assertEqual(467835, result)
