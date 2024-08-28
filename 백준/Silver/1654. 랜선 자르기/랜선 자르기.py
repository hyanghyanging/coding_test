import sys

k, n = map(int, sys.stdin.readline().split())


lan = [int(sys.stdin.readline()) for _ in range(k)]

start = 1  # 랜선의 최소 길이
end = max(lan)  # 랜선의 최대 길이

while start <= end:
    mid = (start + end) // 2   # 중간 값을 기준으로 탐색 범위를 좁힘
    lines = 0 # 랜선의 개수

    for i in lan:
        lines += i // mid   # 자른 랜선의 개수
    
    if lines >= n:      # 필요한 랜선의 개수보다 많은 경우
        start = mid + 1     # 기준부터 끝까지 탐색
    else:               # 필요한 랜선의 개수보다 적은 경우
        end = mid - 1       # 시작부터 기준까지 탐색

print(end)


