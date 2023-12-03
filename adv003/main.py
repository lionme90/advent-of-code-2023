"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

STEPS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
]

NUMBERS = {"0",
           "1",
           "2",
           "3",
           "4",
           "5",
           "6",
           "7",
           "8",
           "9",
           }


def find_adjusted(arr):
    n, m = len(arr), len(arr[0])
    """
       from left to right , from top to bottom
       if found number 
         start append num
            start traversal
             if adjusted symbol is out of boandaries or . or another number
             not adjusted
        
       else 
            end append number
            if not adjusted not add to list
       
    """
    numbers = []
    tmp_num = ""
    adjusted = False
    for x in range(0, n):
        if tmp_num != "":
            if adjusted:
                numbers.append(int(tmp_num))
            tmp_num = ""
            adjusted = False
        for y in range(0, m):
            point = arr[x][y]
            if point in NUMBERS:
                tmp_num += point
                # traverse
                if not adjusted:
                    adjusted = is_adjusted(x, y, arr)
            else:
                if tmp_num != "":
                    if adjusted:
                        numbers.append(int(tmp_num))
                    tmp_num = ""
                    adjusted = False

    return numbers


def is_adjusted(x, y, arr):
    n, m = len(arr), len(arr[0])
    for (xk, yk) in STEPS:
        if 0 <= x + xk < n:
            if 0 <= y + yk < m:
                # print(f"{x + xk}:{y + yk}")
                if arr[x + xk][y + yk] != "." and not arr[x + xk][y + yk] in NUMBERS:
                    return True
    return False


def get_adjusted_gears(x, y, arr, gears):
    n, m = len(arr), len(arr[0])
    adjusted_gears = []
    for (xk, yk) in STEPS:
        if 0 <= x + xk < n:
            if 0 <= y + yk < m:
                if f"{x + xk},{y + yk}" in gears.keys():
                    adjusted_gears.append(f"{x + xk},{y + yk}")
    return adjusted_gears


"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
"""


def find_adjusted_with_gears(arr):
    """
        ok this time there will be data structure

        1 find all gears
        2 find numbers adjusted to a gear
        3 sum number for a gears  where num > 1

        adjusted_gear_x_y -> [numbers]
    """
    gears = {}
    n, m = len(arr), len(arr[0])
    for x in range(0, n):
        for y in range(0, m):
            point = arr[x][y]
            if point == "*":
                gears[f"{x},{y}"] = []
    print(f"gears:{gears}")

    tmp_num = ""
    adj_gears = set()
    for x in range(0, n):
        y = 0
        while y < m:
            # get number
            while y < m and arr[x][y] in NUMBERS:
                tmp_num += arr[x][y]
                adj_gears.update(get_adjusted_gears(x, y, arr, gears))
                y += 1
            if tmp_num.isnumeric():
                for g in adj_gears:
                    gears[g].append(int(tmp_num))
                tmp_num = ""
                adj_gears = set()
            y += 1
    print(f"gears and numbers:{gears}")
    result = 0
    for _, val in gears.items():
        if len(val) > 1:
            mult = 1
            for num in val:
                mult *= num
            result += mult
    return result


if __name__ == '__main__':
    result = 0
    with open("input.txt") as f:
        scheme = []
        for line in f:
            scheme.append(line.rstrip())
    print(find_adjusted(scheme))
    print(f"Result 1 is = {sum(find_adjusted(scheme))}")

if __name__ == '__main__':
    result = 0
    with open("input.txt") as f:
        scheme = []
        for line in f:
            scheme.append(line.rstrip())
    print(find_adjusted(scheme))
    print(f"Result 2 is = {find_adjusted_with_gears(scheme)}")
