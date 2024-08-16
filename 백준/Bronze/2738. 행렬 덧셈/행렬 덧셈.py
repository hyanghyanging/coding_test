import sys

n, m = map(int, sys.stdin.readline().split())

A, B = [], []

for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

for j in range(n):
    B.append(list(map(int, sys.stdin.readline().split())))


for k in range(n):
    for l in range(m):
        print(A[k][l] + B[k][l], end=' ')
    print()  # 줄바꿈