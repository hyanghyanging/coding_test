import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline())

visited = [[-1]*m for _ in range(n)]
def bfs():
    visited[0][0] = 1
    q = deque()
    q.append((0,0))         

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0<=nx<m and 0<=ny<n):
                continue
            
            if arr[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
bfs()
print(visited[n-1][m-1])