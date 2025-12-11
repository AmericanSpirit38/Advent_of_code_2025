def solve(lines):
    res = 0
    for line in lines:
        max1 = -1
        max_idx = -1
        for i in range(len(line)):
            num = int(line[i])
            if num > max1:
                max1 = num
                max_idx = i
        max2 = -1
        if not max_idx + 1 >= len(line):
            for j in range(max_idx + 1, len(line)):
                num = int(line[j])
                if num > max2:
                    max2 = num
        else:
            for j in range(0, max_idx):
                num = int(line[j])
                if num > max2:
                    max2 = num
            max1 , max2 = max2 , max1
        ad = int(str(max1) + str(max2))
        print(ad)
        res += ad

    print(res)

with open('03_input.txt', 'r') as file:
    data = file.read().strip()
    lines = data.split('\n')
    solve(lines)