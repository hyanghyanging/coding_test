import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# dp[i] : i번째 인덱스까지 봤을 때 LIS의 최댓값
dp = [1] * (1000+1)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))