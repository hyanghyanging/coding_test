import sys

n = int(sys.stdin.readline())
step = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * n

if len(step) <= 2:
    print(sum(step))
else:
    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])
    print(dp[-1])