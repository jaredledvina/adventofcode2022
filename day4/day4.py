
#!/usr/bin/env python3
"""
Advent of Code - Day 4
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
    >>> part1(['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8'])
    2
    """
    overlapping_elfs = 0
    for pair in puzzle_input:
        elf1, elf2 = pair.split(',')
        elf1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[-1])+1)
        elf2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[-1])+1)
        if all(item in list(elf1) for item in list(elf2)):
            overlapping_elfs += 1
        elif all(item in list(elf2) for item in list(elf1)):
            overlapping_elfs += 1
    return overlapping_elfs
        

def part2(puzzle_input):
    """
    >>> part2(['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8'])
    4
    """
    overlapping_elfs = 0
    for pair in puzzle_input:
        elf1, elf2 = pair.split(',')
        elf1 = range(int(elf1.split('-')[0]), int(elf1.split('-')[-1])+1)
        elf2 = range(int(elf2.split('-')[0]), int(elf2.split('-')[-1])+1)
        if any(item in list(elf1) for item in list(elf2)):
            overlapping_elfs += 1
        elif any(item in list(elf2) for item in list(elf1)):
            overlapping_elfs += 1
    return overlapping_elfs


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()

