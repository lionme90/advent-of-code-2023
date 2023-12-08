import unittest

from adv007.main import Adv


class TestFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.tested = Adv()
        self.input = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]

    def test_calc_winnings(self):
        self.tested.parse_input(self.input)

        self.assertEqual(1, len(self.tested.hands_by_rank[2]))
        self.assertEqual(2, len(self.tested.hands_by_rank[3]))
        self.assertEqual(2, len(self.tested.hands_by_rank[4]))

        self.assertEqual(6440, self.tested.calc_winnings())

    def test_calc_winnings_with_j(self):
        self.tested.parse_input(self.input, with_jokers=True)

        self.assertEqual(1, len(self.tested.hands_by_rank[2]))
        self.assertEqual(1, len(self.tested.hands_by_rank[3]))
        self.assertEqual(3, len(self.tested.hands_by_rank[6]))

        self.assertEqual(5905, self.tested.calc_winnings())
