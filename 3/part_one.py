import re

with open('puzzle_input.txt') as f:
    data = f.read().strip()
instruction = r'mul\((\d+),(\d+)\)'
valid_numbers = re.findall(instruction, data)
multiplications_sum = sum(int(X) * int(Y) for X, Y in valid_numbers)
print(multiplications_sum)
