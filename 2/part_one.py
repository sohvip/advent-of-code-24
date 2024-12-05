with open('puzzle_input.txt') as f:
    data = f.read().strip().split('\n')
reports = []
for row in data:
    reports.append(row.split(' '))
safe_reports = 0
for report in reports:
    if abs(int(report[0]) - int(report[1])) > 3 or abs(int(report[0]) - int(report[1])) == 0:
        continue
    previous = int(report[1])
    increasing = int(report[0]) < int(report[1])
    safe = True
    for level in report[2:]:
        if increasing:
            if previous < int(level) and int(level) - previous <= 3:
                previous = int(level)
            else:
                safe = False
                break
        else:
            if previous > int(level) and previous - int(level) <= 3:
                previous = int(level)
            else:
                safe = False
                break
    if safe:
        safe_reports += 1
print(f'The number of safe reports: {safe_reports}')
