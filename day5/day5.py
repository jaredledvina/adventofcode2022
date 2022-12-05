
#!/usr/bin/env python3
"""
Advent of Code - Day 5
"""
import os
from textwrap import wrap


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
    >>> part1(['    [D]    ','[N] [C]    ','[Z] [M] [P]',' 1   2   3 ','','move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2'])
    'CMZ'
    """
    stacks = []
    moves = []
    solution = ''
    for line in puzzle_input:
        if '[' in line:
            stacks.append(line)
        elif 'move' in line:
            moves.append(line)
        elif line.startswith(' 1'):
            stack_count = line
    # Each stack is 4 characters wide
    final_stacks = {int(count):[] for count in stack_count.split('  ')}
    for line in stacks:
        row = wrap(line, 4, drop_whitespace=False)
        clean_row = [box.strip().strip('[').strip(']') for box in row]
        for column_count, column in enumerate(clean_row):
            if column != '':
                final_stacks[column_count+1].append(column)
    for move in moves:
        amount, instruction = move.strip('move ').split(' from ')
        amount = int(amount)
        source, destination = instruction.split(' to ')
        source = int(source)
        destination = int(destination)
        for item in range(0, amount):
            final_stacks[destination].insert(0, final_stacks[source].pop(0))
    for column in final_stacks:
        solution += final_stacks[column][0]
    return solution


def part2(puzzle_input):
    """
    >>> part2(['    [D]    ','[N] [C]    ','[Z] [M] [P]',' 1   2   3 ','','move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2'])
    'MCD'
    """
    stacks = []
    moves = []
    solution = ''
    for line in puzzle_input:
        if '[' in line:
            stacks.append(line)
        elif 'move' in line:
            moves.append(line)
        elif line.startswith(' 1'):
            stack_count = line
    # Each stack is 4 characters wide
    final_stacks = {int(count):[] for count in stack_count.split('  ')}
    for line in stacks:
        row = wrap(line, 4, drop_whitespace=False)
        clean_row = [box.strip().strip('[').strip(']') for box in row]
        for column_count, column in enumerate(clean_row):
            if column != '':
                final_stacks[column_count+1].append(column)
    for move in moves:
        amount, instruction = move.strip('move ').split(' from ')
        amount = int(amount)
        source, destination = instruction.split(' to ')
        source = int(source)
        destination = int(destination)
        boxes = []
        for item in range(0, amount):
            boxes.append(final_stacks[source].pop(0))
        final_stacks[destination] = boxes + final_stacks[destination]
    for column in final_stacks:
        solution += final_stacks[column][0]
    return solution


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()

