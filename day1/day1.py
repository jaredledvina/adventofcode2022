#!/usr/bin/env python3
"""
Advent of Code - Day 1
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
    >>> part1([1000,2000,3000,'',4000,'',5000,6000,'',7000,8000,9000,'',10000])
    24000
    """
    elves_calories = {}
    elf_id = 1
    calories = 0
    for entry in puzzle_input:
        if entry != '':
            calories += int(entry)
        else:
            elves_calories[elf_id] = calories
            elf_id += 1
            calories = 0
    elves_calories[elf_id] = calories
    return max(elves_calories.values())


def part2(puzzle_input):
    """
    >>> part2([1000,2000,3000,'',4000,'',5000,6000,'',7000,8000,9000,'',10000])
    45000
    """
    elves_calories = {}
    elf_id = 1
    calories = 0
    for entry in puzzle_input:
        if entry != '':
            calories += int(entry)
        else:
            elves_calories[elf_id] = calories
            elf_id += 1
            calories = 0
    elves_calories[elf_id] = calories
    return sum(sorted(elves_calories.values(), reverse=True)[:3])


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
