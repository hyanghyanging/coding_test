import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]   # 위, 아래
    dy = [0, 0, -1, 1]   # 왼쪽, 오른쪽
    queue = deque()
    queue.append((x, y))  # 시작점 추가
    graph[x][y] = 0       # 방문 처리 
    cnt = 1 

    while queue:
        x, y = queue.popleft() # 큐에서 탐색할 노드를 꺼냄

        for i in range(4):
            nx = x + dx[i] # 다음 위치의 x 좌표
            ny = y + dy[i] # 다음 위치의 y 좌표

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1: # 연결된 집이 있는 경우
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny)) # 다음 탐색을 위해 큐에 추가
                cnt += 1               # 단지 내 집의 수 증가
    return cnt

# 지도 전체를 순회하면서 단지를 찾고, 각 단지의 집 개수를 기록
count = [bfs(graph, i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

# 각 단지 내 집의 수를 오름차순으로 정렬
count.sort()
# 총 단지 수 출력
print(len(count))

# 각 단지 내 집의 수를 한 줄씩 출력
for i in range(len(count)):
    print(count[i])