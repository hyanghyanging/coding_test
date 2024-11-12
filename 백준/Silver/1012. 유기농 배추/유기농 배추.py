import sys

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0] # 상하좌우 이동을 위한 x 좌표 변화량
dy = [0, 0, -1, 1] # 상하좌우 이동을 위한 y 좌표 변화량

def BFS(x, y):
    queue = [(x, y)]  # 초기 위치를 큐에 넣음
    matrix[x][y] = 0  # 방문처리. 이미 탐색한 배추는 0으로 만들기

    while queue:
        x, y = queue.pop(0) # 큐의 첫번째 요소를 꺼내며 탐색 시작

        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N: # 이동한 위치가 배추밭 내에 있는지 확인
                continue

            if matrix[nx][ny] == 1:    # 인접한 위치에 배추가 있을 경우
                queue.append((nx, ny)) # 인접한 배추 위치를 큐에 추가
                matrix[nx][ny] = 0     # 방문 처리하여 0으로 만듦

# 테스트 케이스 수만큼 반복
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split()) # 배추밭의 가로, 세로 길이, 배추 개수
    matrix = [[0]*N for _ in range(M)] # 배추밭 생성. 배추가 없으면 0
    cnt = 0 # 필요한 지렁이의 개수

    for j in range(K): # 배추가 심어져 있는 위치 설정
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1 # 배추 위치를 1로 표시
    
    for a in range(M): # 배추밭을 순회하며 배추 그룹 찾기
        for b in range(N):
            if matrix[a][b] == 1: # 아직 탐색되지 않은 배추가 있을 경우
                BFS(a,b) # BFS로 해당 배추와 인접한 모든 배추를 방문 처리
                cnt += 1 # 한 번의 BFS 탐색이 끝날때마다 지렁이 하나가 필요함
    
    print(cnt)