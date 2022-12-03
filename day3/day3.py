
#!/usr/bin/env python3
"""
Advent of Code - Day 3
"""
import os
import string


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
    >>> part1(['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw'])
    157
    """
    priorities = dict(zip(list(string.ascii_lowercase), [ord(letter)-96 for letter in string.ascii_lowercase]))
    priorities.update(dict(zip(list(string.ascii_uppercase), [ord(letter)-38 for letter in string.ascii_uppercase])))

    bad_items = 0
    for rucksack in puzzle_input:
        one, two = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for item in one:
            if item in two:
                bad_items += priorities[item]
                break
    return bad_items


def part2(puzzle_input):
    """
    >>> part2(['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw'])
    70
    """
    priorities = dict(zip(list(string.ascii_lowercase), [ord(letter)-96 for letter in string.ascii_lowercase]))
    priorities.update(dict(zip(list(string.ascii_uppercase), [ord(letter)-38 for letter in string.ascii_uppercase])))

    badges = 0
    while len(puzzle_input) > 0:
        one, two, three = puzzle_input.pop(0), puzzle_input.pop(0), puzzle_input.pop(0)
        for item in one:
            if item in two:
                if item in three:
                    badges += priorities[item]
                    break
    return badges


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
    

if __name__ == '__main__':
    main()

