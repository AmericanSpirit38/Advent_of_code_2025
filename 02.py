def solve(inp):
    res = 0
    for ids in inp:
        ranges = list(ids.strip().split('-'))
        for i in range(int(ranges[0]), int(ranges[1]) + 1):
            if len(str(i)) % 2 == 0:
                part1, part2 = str(i)[:len(str(i)) // 2], str(i)[len(str(i)) // 2:]
                if part1 == part2:
                    res += i
    return res


with open('02_input.txt', 'r') as file:
    data = file.read()
    inp = data.split(',')
    print(solve(inp))