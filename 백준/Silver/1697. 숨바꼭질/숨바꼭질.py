import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [0] * (100000+1) # 각 위치에 도달할 때까지 걸린 시간

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0<= j <= 100000 and not visited[j]: # 이때, not visited[j] 와 visited[j] == 0은 같은 의미
                visited[j] = visited[x] + 1
                q.append(j)

bfs()