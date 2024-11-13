import sys
from collections import deque

def bfs(start):
    queue = deque([start])  # 시작 정점을 큐에 추가
    visited[start] = True   # 시작 정점을 방문처리
    while queue:
        node = queue.popleft() # 큐의 맨 앞에 있는 정점을 꺼냄
        for i in graph[node]:  # 현재 정점에 연결된 모든 인접 노드 탐색
            if not visited[i]:    # 인접 노드가 방문되지 않았다면
                visited[i] = True # 방문처리
                queue.append(i)   # 큐에 추가

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] # 연결 리스트를 저장할 그래프 생성

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v) # u -> v
    graph[v].append(u) # v -> u : 무방향 그래프이므로 양방향 연결

# 방문처리
visited = [False] * (1 + N)
count = 0

# 모든 정점을 순회하며 연결 요소 찾기
for i in range(1, N+1):
    if not visited[i]: # 정점이 방문되지 않은 경우
        if not graph[i]:  # 해당 정점이 다른 정점과 연결되지 않은 경우
            count += 1    # 하나의 연결 요소로 취급
            visited[i] = True # 방문처리
        else:
            bfs(i) # bfs로 연결된 모든 정점을 방문 처리
            count += 1 # bfs 탐색을 통해 하나의 연결 요소 탐색이 완료되었으므로 카운트 증가

print(count)