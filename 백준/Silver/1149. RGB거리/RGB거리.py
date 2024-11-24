import sys

n = int(sys.stdin.readline())
a = [0]*n

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))

for j in range(1, n):
    a[j][0] = min(a[j-1][1], a[j-1][2]) + a[j][0]
    a[j][1] = min(a[j-1][0], a[j-1][2]) + a[j][1]
    a[j][2] = min(a[j-1][0], a[j-1][1]) + a[j][2]

print(min(a[n-1][0], a[n-1][1], a[n-1][2]))