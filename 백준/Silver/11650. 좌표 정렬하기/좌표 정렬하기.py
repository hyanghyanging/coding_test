import sys

n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
points.sort()

for i in range(n):
    print(points[i][0], points[i][1])