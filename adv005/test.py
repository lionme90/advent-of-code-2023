import unittest

from adv005.main import Adv


class TestFunction(unittest.TestCase):

    def setUp(self) -> None:
        self.tested = Adv()
        self.input = [
            "seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
            "",
            "water-to-light map:",
            "88 18 7",
            "18 25 70",
            "",
            "light-to-temperature map:",
            "45 77 23",
            "81 45 19",
            "68 64 13",
            "",
            "temperature-to-humidity map:",
            "0 69 1",
            "1 0 69",
            "",
            "humidity-to-location map:",
            "60 56 37",
            "56 93 4",
        ]

    def test_find_location(self):
        self.tested.parse_seeds_simple(self.input[0])
        self.tested.parse_input(self.input)

        self.assertEqual(4, len(self.tested.seeds))
        self.assertEqual(2, len(self.tested.maps_data["seed-to-soil"]))
        self.assertEqual(3, len(self.tested.maps_data["seed-to-soil"][0]))
        self.assertEqual(3, len(self.tested.maps_data["soil-to-fertilizer"]))
        self.assertEqual(4, len(self.tested.maps_data["fertilizer-to-water"]))
        self.assertEqual(2, len(self.tested.maps_data["water-to-light"]))
        self.assertEqual(3, len(self.tested.maps_data["light-to-temperature"]))
        self.assertEqual(2, len(self.tested.maps_data["temperature-to-humidity"]))
        self.assertEqual(2, len(self.tested.maps_data["humidity-to-location"]))

        expected = [82, 43, 86, 35]
        res_seeds = []
        for i, seed in enumerate(self.tested.seeds):
            res_seed = self.tested.find_location(seed)
            res_seeds.append(res_seed)
            self.assertEqual(expected[i], self.tested.find_location(seed))

        self.assertEqual(35, min(res_seeds))

    def test_find_more_seeds(self):
        self.tested.parse_seeds(self.input[0])
        self.tested.parse_input(self.input)
        self.assertEqual(2, len(self.tested.ranges))
        self.assertEqual(46, self.tested.find_range_location())
