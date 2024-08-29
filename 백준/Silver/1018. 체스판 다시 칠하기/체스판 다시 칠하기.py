import sys

n, m = map(int, sys.stdin.readline().split())
board = []
result = []
for _ in range(n):
    board.append(str(sys.stdin.readline().strip()))

for i in range(n-7):    # i, j : 보드의 시작점
    for j in range(m-7):
        first_W = 0  # W로 시작할 때 색칠해야 하는 부분의 개수
        first_B = 0  # B로 시작할 때 색칠해야 하는 부분의 개수
        for x in range(i, i+8): 
            for y in range(j, j+8):  
                if (x+y) % 2 == 0: # 짝수인 경우 처음 색과 같아야 함.
                    if board[x][y] != 'W':  # W가 아닌 경우 = B인 경우
                        first_W += 1        # W로 칠함
                    if board[x][y] != 'B':  # B가 아닌 경우 = W인 경우
                        first_B += 1        # B로 칠함
                else:
                    if board[x][y] != 'B':  # B가 아닌 경우 = W인 경우
                        first_W += 1        # W로 칠함
                    if board[x][y] != 'W':  # W가 아닌 경우 = B인 경우
                        first_B += 1        # B로 칠함
        result.append(first_W)
        result.append(first_B)

print(min(result))