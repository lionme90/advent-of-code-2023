"""

--- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
52 50 48
50 98 2

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
42 0 7
57 7 4
0 11 42
49 53 8

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?


--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?


"""

from typing import List


class Adv:

    def __init__(self):
        self.maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
                     "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
        self.seeds = []
        self.maps_data = {}
        self.ranges = []

    def parse_seeds_simple(self, seeds_line: str):
        self.seeds = [map(int, seed) for seed in seeds_line.split(": ")[1].split(" ")]

    def parse_seeds(self, seeds_line: str):
        raw_seeds = seeds_line.split(": ")[1].split(" ")
        for i in range(0, len(raw_seeds), 2):
            rang = (int(raw_seeds[i]), int(raw_seeds[i + 1]) + int(raw_seeds[i]))
            self.ranges.append(rang)

    def parse_input(self, input: List[str]):
        result = {}
        i = 2
        while i < len(input):
            line = input[i].rstrip()
            if line.endswith(" map:"):
                block_name = line.split(" ")[0]
                result[block_name] = []
                i += 1
                while line != "" and i < len(input):
                    line = input[i].rstrip()
                    if line != "":
                        result[block_name].append([int(val.rstrip()) for val in line.split(" ")])
                    i += 1
        self.maps_data = result

    def find_location(self, seed: int, map_idx=0) -> int:
        if map_idx < len(self.maps):
            for destination, source, interval_len in self.maps_data[self.maps[map_idx]]:
                interval_end = source + interval_len
                if source <= seed <= interval_end:
                    destination_seed = (seed - source) + destination
                    return self.find_location(destination_seed, map_idx + 1)
            return self.find_location(seed, map_idx + 1)
        else:
            return seed

    def find_range_location(self) -> int:
        locations = []
        for start_range, end_range in self.ranges:
            ranges_q = [(start_range, end_range)]
            results = []
            for map_idx in self.maps:
                while ranges_q:
                    start_range, end_range = ranges_q.pop()
                    for destination, source, interval_len in self.maps_data[map_idx]:
                        interval_end = source + interval_len
                        offset = destination - source
                        if interval_end <= start_range or end_range <= source:
                            continue
                        if start_range < source:
                            ranges_q.append((start_range, source))
                            start_range = source
                        if interval_end < end_range:
                            ranges_q.append((interval_end, end_range))
                            end_range = interval_end
                        results.append((start_range + offset, end_range + offset))
                        break
                    else:
                        results.append((start_range, end_range))
                ranges_q = results
                results = []
            locations += ranges_q
        return min(loc[0] for loc in locations)


if __name__ == '__main__':
    adv = Adv()
    with open("input.txt") as f:
        input = []
        for line in f:
            input.append(line)
    adv.parse_input(input)
    # results = []
    # adv.parse_seeds_simple(input[0])
    # for seed in adv.seeds:
    #     results.append(adv.find_location(seed))
    # print(f"Result is = {min(results)}")

    adv.parse_seeds(input[0])
    result = adv.find_range_location()
    print(f"Result is = {result}")
