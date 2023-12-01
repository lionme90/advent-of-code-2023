"""
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""
from typing import List

DIGITS = {"zero": "0",
          "one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9",
          }


def get_calibration_value(arr: List[str]):
    result = 0
    for line in arr:
        result += calc_line(line)
    return result


def calc_line(line: str):
    """
     # two pointers
    # case 1 zoneight234
             ^      ^
               ^
    sliding window
    # zoneight
         ^
       ^
      if pointer > than 5 I need to start decreasing by - 1
    """
    left, right = 0, len(line) - 1
    d_left = ""
    d_right = ""
    while left <= right:
        left_start = 0
        while left_start <= left:
            w_digit = line[left_start:left]
            if w_digit in DIGITS:
                d_left = DIGITS[w_digit]
                break
            else:
                left_start += 1
        if not d_left.isnumeric():
            if not line[left].isnumeric():
                left += 1
            else:
                d_left = line[left]

        right_end = len(line)

        while right_end >= right:
            w_digit = line[right:right_end]
            if w_digit in DIGITS:
                d_right = DIGITS[w_digit]
                break
            else:
                right_end -= 1

        if not d_right.isnumeric():
            if not line[right].isnumeric():
                right -= 1
            else:
                d_right = line[right]

        if d_left.isnumeric() and d_right.isnumeric():
            break

    result = d_left + d_right
    return 0 if result == "" else int(result)


if __name__ == '__main__':
    result = 0
    with open("adv001/input.txt") as f:
        for line in f:
            result += calc_line(line)

    print(f"Result is = {result}")
