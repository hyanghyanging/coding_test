import sys
from collections import deque

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
hands = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

deq = deque(hands)

for i in range(t):
    deq.rotate(1-b[i])
    print(deq[0], end=' ')
