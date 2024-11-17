import sys

n = int(sys.stdin.readline())
# 회의가 빨리 끝나는 순서대로 정렬해야 함 -> 회의를 최대한 많이 하기 위한 전략
meet = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x:[x[1], x[0]])
cnt = end = 0
for s, e in meet:
    if s >= end:
        cnt += 1
        end = e
print(cnt)