from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    visited = [-1]*(n+1)

    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)

    total = sum(visited)
    return total

min_total = float("INF")
ans = 0
for i in range(1, n+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        ans = i

print(ans)