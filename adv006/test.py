import unittest

from adv006.main import Adv


class TestFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.tested = Adv()
        self.input = [
            "Time:      7  15   30\n",
            "Distance:  9  40  200\n"
        ]

    def test_find_ways_to_win(self):
        self.tested.parse_input(self.input)

        self.assertEqual(len(self.tested.times), len(self.tested.distances))
        self.assertEqual(3, len(self.tested.distances))

        result = [4, 8, 9]
        i = 0
        for time, distance in zip(self.tested.times, self.tested.distances):
            self.assertEqual(result[i], self.tested.count_ways_to_win(time, distance))
            i += 1
