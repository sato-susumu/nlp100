path = './data/popular-names.txt'
N = 5
with open(path) as f:
    lines = f.readlines()

    unit_size = int(len(lines) / N)
    start = 0
    while start < len(lines):
        for line in lines[start:start + unit_size]:
            print(line[:-1])
        print('')
        start += unit_size

print('macのsplitはN分割オプションがないため、splitコマンドでの実現はスキップ')
