import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))
V = int(input())
print(L.count(V))