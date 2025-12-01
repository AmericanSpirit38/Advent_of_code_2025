def normalize_position(pos):
    if 0 <= pos <= 99:
        return pos
    elif pos < 0:
        pos = 100 - abs(pos)
        return normalize_position(pos)
    else:  # pos > 99
        pos = pos - 100
        return normalize_position(pos)


def solve(commands):
    pos = 50
    res = 0
    for command in commands:
        direction, value = command[:1], int(command[1:])
        direction = 1 if direction == 'R' else -1
        pos += direction * value
        pos = normalize_position(pos)
        if pos == 0:
            res += 1
    return res

with open('01_input.txt', 'r') as file:
    data = file.read()
    commands = [line for line in data.splitlines()]
    print(solve(commands))