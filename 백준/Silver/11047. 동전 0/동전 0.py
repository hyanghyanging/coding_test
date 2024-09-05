import sys

n, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0
a.reverse()

for coin in a:
    cnt += k // coin
    k = k % coin
    if k <= 0:
        break

print(cnt)