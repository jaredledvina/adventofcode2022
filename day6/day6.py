
#!/usr/bin/env python3
"""
Advent of Code - Day 6
"""
import os


def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input


def part1(puzzle_input):
    """
    >>> part1(['mjqjpqmgbljsphdztnvjfqwrcgsmlb'])
    7
    >>> part1(['bvwbjplbgvbhsrlpgdmjqwftvncz'])
    5
    >>> part1(['nppdvjthqldpwncqszvftbrmjlhg'])
    6
    >>> part1(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'])
    10
    >>> part1(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'])
    11
    """
    datastream = puzzle_input[0]
    marker = []
    for position, character in enumerate(datastream):
        marker.append(character)
        if len(marker) >= 4:
            if len(set(marker[-4:])) == 4:
                break
    return position +1


def part2(puzzle_input):
    """
    >>> part2(['mjqjpqmgbljsphdztnvjfqwrcgsmlb'])
    19
    >>> part2(['bvwbjplbgvbhsrlpgdmjqwftvncz'])
    23
    >>> part2(['nppdvjthqldpwncqszvftbrmjlhg'])
    23
    >>> part2(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'])
    29
    >>> part2(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'])
    26
    """
    datastream = puzzle_input[0]
    marker = []
    for position, character in enumerate(datastream):
        marker.append(character)
        if len(marker) >= 14:
            if len(set(marker[-14:])) == 14:
                break
    return position +1


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()

