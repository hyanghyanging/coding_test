import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(h)]
# 익은 토마토의 좌표를 담을 deque
q = deque()

dx = [1, -1, 0, 0, 0, 0] # 좌우로 이동
dy = [0, 0, 1, -1, 0, 0] # 상하로 이동
dz = [0, 0, 0, 0, 1, -1] # 위아래로 이동

# 익은 토마토를 찾아서 deque에 넣기
for i in range(h):           # 높이
    for j in range(n):       # 세로
        for k in range(m):   # 가로
            if box[i][j][k] == 1:     # 익은 토마토일 경우
                q.append((i, j, k))   # 익은 토마토의 좌표를 deque에 넣기

# bfs로 토마토가 익는 과정 탐색
def bfs():
    while q:                         # deque가 빌 때까지 = 모든 토마토가 익을 때까지
        z, x, y = q.popleft()        # 먼저 들어온 순서대로 pop
        for i in range(6):           # 상하좌우위아래의 6방향 탐색
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]  # 새로운 좌표
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1  # 익은 상태로 바꾸기
                q.append((nz, nx, ny))              # 새로 익은 토마토의 좌표를 deque에 넣기
    
    # 모든 토마토가 익었는지 확인
    max_day = 0   # 최대 일수
    for i in box: 
        for j in i:
            for k in j:
                if k == 0:  # 익지 않은 토마토가 있을 경우
                    return -1 
                max_day = max(max_day, k)  # 최대 일수 갱신
    return max_day - 1 # 첫날부터 시작했으므로 1을 빼줌


print(bfs())