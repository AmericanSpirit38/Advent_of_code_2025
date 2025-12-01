def solve(commands):
    pos = 50
    res = 0

    for cmd in commands:
        step = int(cmd[1:])
        dir = 1 if cmd[0] == "R" else -1
        step *= dir
        res += (abs(pos + step) // 100 + (pos != 0)) if pos + step <= 0 else ((pos + step) // 100 if pos + step > 99 else 0)
        pos = (pos + step) % 100
    return res


with open('01_input.txt', 'r') as file:
    data = file.read()
    commands = [line for line in data.splitlines()]
    print(solve(commands))