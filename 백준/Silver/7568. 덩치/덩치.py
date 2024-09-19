import sys

n = int(sys.stdin.readline().strip())
biggest = 0
big = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    big.append([x, y])

for size in big:
    rank = 1
    for i in big:
        if size[0] < i[0] and size[1] < i[1]:
            rank += 1
    print(rank, end=' ')  # 옆으로 출력
