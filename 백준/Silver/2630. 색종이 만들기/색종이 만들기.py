import sys
'''
분할 정복 알고리즘
큰 문제를 작은 문제로 분할하여 문제를 풀고 다시 합치는 알고리즘

*재귀함수 활용*
'''

n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []

def solution(x, y, N):
    color = paper[x][y]  # 현재 영역의 왼쪽 위의 색이 기준
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:  # 현재 조사 중인색과 다르다면, 영역 4등분
                solution(x, y, N//2)           # 왼쪽 위
                solution(x, y+N//2, N//2)      # 오른족 위
                solution(x+N//2, y, N//2)      # 왼쪽 아래
                solution(x+N//2, y+N//2, N//2) # 오른쪽 아래
                return
    if color == 0: # 모든 좌표가 같은 색을 가지고 있다면 해당 색을 결과 리스트에 추가
        result.append(0)
    else:
        result.append(1)

solution(0, 0, n)
print(result.count(0))  # 하얀 색종이의 개수
print(result.count(1))  # 파란 색종이의 개수

            