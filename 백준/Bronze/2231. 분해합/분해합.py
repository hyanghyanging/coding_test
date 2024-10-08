import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    num = sum(map(int, str(i)))  # 각 자리수 더하기
    result = i + num  
    if result == n:  # 생성자를 찾은 경우
        print(i)
        break
    if i == n: # 생성자가 없다면
        print(0)