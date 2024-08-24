import sys

N = int(sys.stdin.readline())
boj = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    boj.append((int(age), name))

boj.sort(key=lambda x: x[0])

for i in boj:
    print(i[0], i[1])
