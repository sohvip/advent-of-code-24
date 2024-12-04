with open('puzzle_input.txt') as f:
    data = f.read().strip().split('\n')
left, right = [], []
for row in data:
    pair = row.split('   ')
    left.append(int(pair[0]))
    right.append(int(pair[1]))
for i, num in enumerate(left):
    multiplier = 0
    for j in right:
        if j == num:
            multiplier += 1
    left[i] = num * multiplier
print(f'The similarity score: {sum(left)}')
