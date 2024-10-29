import sys
'''
다이나믹 프로그래밍에서의 핵심은 수학 점화식 찾기!
'''
n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 맨 앞
            triangle[i][j] += triangle[i-1][j]
        elif j == i: # 맨 뒤
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))