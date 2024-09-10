import sys

n = int(sys.stdin.readline())
coordinates = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x, y])

coordinates.sort(key=lambda x: (x[1], x[0]))

for j in coordinates:
    print(j[0], j[1])