import sys
from collections import deque

T = int(sys.stdin.readline())


for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    queue = deque([(idx, val) for idx, val in enumerate(importance)])
    cnt = 0

    while queue:
        if queue[0][1] < max(queue, key=lambda x: x[1])[1]:
            queue.rotate(-1)
        else:
            cnt += 1
            if queue[0][0] == m:
                print(cnt)
                break
            else:
                queue.popleft()