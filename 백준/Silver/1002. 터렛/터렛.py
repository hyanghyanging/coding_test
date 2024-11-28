import sys
import math

t = int(sys.stdin.readline())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2: # 같은 원 
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance: # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2): # 서로 다른 두 점
        print(2)
    else:
        print(0) # 만나지 않음
