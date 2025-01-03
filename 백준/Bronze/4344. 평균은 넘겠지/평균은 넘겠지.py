import sys

c = int(sys.stdin.readline().strip())

for i in range(c):
    n, *scores = map(int, sys.stdin.readline().split())
    avg = sum(scores) / n
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    print(f'{cnt / n * 100:.3f}%')