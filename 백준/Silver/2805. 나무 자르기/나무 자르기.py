import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)  # 짦은 길이:start, 긴 길이: end

while start <= end:
    mid = (start+end) // 2
    log = 0 # 벌목된 나무 총합
    for i in trees:
        if i >= mid:
            log += i - mid
        
    # 벌목 높이를 이분탐색
    if log >= m:  # 목표보다 크거나 작은 경우 
        start = mid + 1 # 높이를 높임
    else:
        end = mid - 1
        
print(end)