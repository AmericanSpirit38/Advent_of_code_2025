def max_subsequence_number(s, k):
    to_remove = len(s) - k
    stack = []
    for ch in s:
        while stack and to_remove > 0 and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)
    if to_remove > 0:
        stack = stack[:-to_remove]
    return int(''.join(stack[:k]))

def solve_line(line):
    result = max_subsequence_number(line, 12)
    print(str(result).rjust(12, '0'))  # print the chosen 12-digit result (keeps leading zeros if any)
    return result

def solve(lines):
    res = 0
    for line in lines:
        res += solve_line(line.strip())
    print(res)

with open('03_input.txt', 'r') as file:
    data = file.read().strip()
    lines = data.split('\n')
    solve(lines)
