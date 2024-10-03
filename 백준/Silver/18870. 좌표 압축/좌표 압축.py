import sys

n = int(sys.stdin.readline())

coordinates = list(map(int, sys.stdin.readline().strip().split()))
sort_coord = sorted(list(set(coordinates)))

dic = {sort_coord[i] : i for i in range(len(sort_coord))}
for j in coordinates:
    print(dic[j], end=' ')