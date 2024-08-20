import sys

n = int(sys.stdin.readline())
cnt = 0   # 666이 포함된 숫자 카운트
num = 666

while True:
    if '666' in str(num):
        cnt += 1
    
    if cnt == n:
        break

    num += 1

print(num)
