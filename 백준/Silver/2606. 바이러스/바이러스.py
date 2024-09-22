import sys

v = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())

# 인접 리스트 사용하기
adj_list = [[] for _ in range(v+1)]
visited = [0] * (v+1)  # 방문 기록

for _ in range(e):  # 간선 개수만큼 연결 정보를 받음
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향 그래프이기 때문

def dfs(e):
    visited[e] = 1
    for nx in adj_list[e]:
        if visited[nx] == 0:  # 방문하지 않은 노드이면
            dfs(nx)           # 탐색

dfs(1)
print(sum(visited)-1)  # 1번 컴퓨터를 제외하고 1번 컴퓨터와 연결된 컴퓨터의 개수 출력