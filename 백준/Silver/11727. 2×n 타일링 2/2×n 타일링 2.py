import sys
n = int(sys.stdin.readline())
dp = [0] * 1001
dp[0] = 1
dp[1] = 1
for i in range(2, 1001):
    dp[i] = (dp[i-1] + 2 * dp[i-2])

print(dp[n] % 10007)
