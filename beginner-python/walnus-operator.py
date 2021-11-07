lines = []

def canAdd(max=5):
    global lines
    if allowed := (count := len(lines))< max:
        print(f'you can enter{max-count} more')
    return allowed

while canAdd():
    lines.append(l := input('Enter a line: '))
print(f'You entered": {lines}') 