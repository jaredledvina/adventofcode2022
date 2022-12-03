#!/usr/bin/env python3
"""
Advent of Code - Day N
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
    >>> part1(['A Y','B X','C Z'])
    15
    """
    score = 0
    for game in puzzle_input:
        elf, me = game.split(' ')
        if me == 'X':
            score += 1
            if elf == 'A':
                score += 3
            elif elf == 'B':
                score += 0
            elif elf == 'C':
                score += 6
        elif me == 'Y':
            score += 2
            if elf == 'A':
                score += 6
            elif elf == 'B':
                score += 3
            elif elf == 'C':
                score += 0
        elif me == 'Z':
            score += 3
            if elf == 'A':
                score += 0
            elif elf == 'B':
                score += 6
            elif elf == 'C':
                score += 3
    return score


def part2(puzzle_input):
    """
    >>> part2(['A Y','B X','C Z'])
    12
    """
    score = 0
    for game in puzzle_input:
        elf, me = game.split(' ')
        if me == 'X':
            score += 0
            if elf == 'A':
                score += 3
            elif elf == 'B':
                score += 1
            elif elf == 'C':
                score += 2
        elif me == 'Y':
            score += 3
            if elf == 'A':
                score += 1
            elif elf == 'B':
                score += 2
            elif elf == 'C':
                score += 3
        elif me == 'Z':
            score += 6
            if elf == 'A':
                score += 2
            elif elf == 'B':
                score += 3
            elif elf == 'C':
                score += 1
    return score
    return 


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
