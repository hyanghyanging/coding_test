import sys

k = int(input())
L = []

for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        L.pop()
    else:
        L.append(num)

print(sum(L))