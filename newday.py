#!/usr/bin/env python3
"""
Advent of Code - Day generator
"""
import os

DAY = '3'

PYTHON_START = '''
#!/usr/bin/env python3
"""
Advent of Code - Day ''' + DAY + '''
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
    >>> part1([])
    
    """
    return


def part2(puzzle_input):
    """
    >>> part2([])
    
    """
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

'''

def main():
    os.mkdir('day' + DAY, 0o755)
    with open('day' + DAY + '/input.txt', 'w') as f:
        pass
    with open('day' + DAY + '/' + 'day' + DAY + '.py', 'w') as f:
        f.write(PYTHON_START)
    os.chmod('day' + DAY + '/' + 'day' + DAY + '.py', 0o755)

if __name__ == '__main__':
    main()
