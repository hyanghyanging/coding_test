import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())
array = deque([i for i in range(1, N+1)])
direction = 1   # 시계방향 : 1, 반시계방향 : -1
remove_num = 0    # 제거된 횟수 기록

while array:
    if direction == 1:  # 시계방향
        array.rotate(-(K-1))   # 반시계방향으로 (k-1)칸 이동
    else:
        array.rotate(K)        # 시계방향으로 K칸 이동

    result = array.popleft()
    remove_num += 1

    # M번째 제거 마다 방향 전환
    if remove_num % M == 0:
        direction *= -1
    
    print(result)