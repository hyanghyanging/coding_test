import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
interval_sum = [0]
tmp = 0

# 누적합
for num in nums:
    tmp += num
    interval_sum.append(tmp)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(interval_sum[j] -interval_sum[i-1])