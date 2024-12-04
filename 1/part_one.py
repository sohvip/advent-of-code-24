with open('puzzle_input.txt') as f:
    data = f.read().strip().split('\n')
left, right = [], []
for row in data:
    pair = row.split('   ')
    left.append(int(pair[0]))
    right.append(int(pair[1]))
left.sort()
right.sort()
distances = []
for i in range(len(left)):
    distance = abs(left[i] - right[i])
    distances.append(distance)
print(f'The total distance between the lists: {sum(distances)}')
