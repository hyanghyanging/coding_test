import sys

n = int(sys.stdin.readline())
prepared = list(sys.stdin.readline().split())
used = list(sys.stdin.readline().split())

for i in prepared:
    if i not in used:
        print(i)