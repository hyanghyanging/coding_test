import sys, math

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int,sys.stdin.readline().split())

shirts_set = 0
for i in range(len(sizes)):
    if sizes[i] > 0:
        shirts_set += math.ceil(sizes[i]/t)

print(shirts_set)
print(n//p, n%p)