import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    
    dp_0 = [0] * (40+1)
    dp_1 = [0] * (40+1)

    dp_0[0] = 1
    dp_1[1] = 1
    
    for i in range(2, n+1):
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]

    print(dp_0[n], dp_1[n])
