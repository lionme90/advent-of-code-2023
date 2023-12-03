import unittest

from adv002.main import is_game_possible, parse_input, get_minimum_required_cubes


class TestFunction(unittest.TestCase):

    def test_calc_game_2(self):
        cases = [
            "Game 1: 4 green, 2 blue; 1 red, 1 blue, 4 green; 3 green, 4 blue, 1 red; 7 green, 2 blue, 4 red; 3 red, 7 green; 3 red, 3 green",
            "Game 2: 1 blue, 11 red, 1 green; 3 blue, 2 red, 4 green; 11 red, 2 green, 2 blue; 13 green, 5 red, 1 blue; 4 green, 8 red, 3 blue",
            "Game 3: 9 red, 2 blue; 4 blue, 2 green, 1 red; 7 red, 4 blue, 3 green; 3 blue, 6 red; 9 blue, 4 red; 3 red",
            "Game 3: 9 red, 2 blue; 4 blue, 2 green, 1 red; 7 red, 4 blue, 3 green; 3 blue, 6 red; 9 blue, 4 red; 3 red",
            "Game 5: 3 green, 7 blue, 7 red; 6 green, 3 red, 4 blue; 7 blue, 4 red",
        ]

        parsed_cases = []
        for case in cases:
            parsed_cases.append(parse_input(case))

        results = [
            True,
            True,
            True,
            True,
            True
        ]
        sum = 0
        for i, case in enumerate(parsed_cases):
            self.assertEqual(results[i], is_game_possible(case["plays"]), case)
            if is_game_possible(case["plays"]):
                sum += case["index"]
        self.assertEqual(14, sum)

        """

        """

    def test_calc_game(self):
        cases = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        parsed_cases = []
        for case in cases:
            parsed_cases.append(parse_input(case))

        results = [
            True,
            True,
            False,
            False,
            True
        ]
        sum = 0
        for i, case in enumerate(parsed_cases):
            self.assertEqual(results[i], is_game_possible(case["plays"]), case)
            if is_game_possible(case["plays"]):
                sum += case["index"]
        self.assertEqual(8, sum)

    def test_minimum_possible(self):
        cases = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        parsed_cases = []
        for case in cases:
            parsed_cases.append(parse_input(case))
        results = [
            48,
            12,
            1560,
            630,
            36
        ]

        sum = 0
        for i, case in enumerate(parsed_cases):
            self.assertEqual(results[i], get_minimum_required_cubes(case["plays"]), case)
            sum += get_minimum_required_cubes(case["plays"])

        self.assertEqual(2286, sum)
