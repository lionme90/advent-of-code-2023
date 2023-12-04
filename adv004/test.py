import unittest

from adv004.main import Adv


class TestFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.tested = Adv()

    def test_calculate_card_worth(self):
        cases = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]

        results = [
            8,
            2,
            2,
            1,
            0,
            0
        ]
        sum = 0
        for i, case in enumerate(cases):
            result = self.tested.calc_card_worth(case)
            sum += result
            self.assertEqual(results[i], result, case)

        self.assertEqual(13, sum)

    def test_calculate_total_cards_won(self):
        cases = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        parsed_cases = [self.tested.parse_card_string(case) for case in cases]
        self.assertEqual(30, self.tested.total_cards_won(parsed_cases))
