def if_divisible(a, b):
    return a % b == 0

def get_parts(n, num, ln):
    parts = []
    num = str(num)
    for i in range(0, n, ln):
        parts.append(num[i:i + ln])
    return parts

def check_repeat(n, num, ln):
    parts = get_parts(n, num, ln)
    return len(set(parts)) == 1

def solve(inp):
    res = 0
    for ids in inp:
        ranges = list(ids.strip().split('-'))
        start = int(ranges[0])
        end = int(ranges[1])
        for num in range(start, end + 1):
            s = str(num)
            L = len(s)
            for i in range(L // 2):
                ln = i + 1
                if if_divisible(L, ln):
                    if check_repeat(L, num, ln):
                        res += num
                        break
    return res

with open('02_input.txt', 'r') as file:
    data = file.read()
    inp = data.split(',')
    print(solve(inp))
