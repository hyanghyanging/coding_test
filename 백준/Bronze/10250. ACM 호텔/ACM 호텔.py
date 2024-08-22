import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N%H == 0:
        floor = H
        room = N//H
    else:
        floor = N%H
        room = N//H + 1
        
    print(floor*100 + room)