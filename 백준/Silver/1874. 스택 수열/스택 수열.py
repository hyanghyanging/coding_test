import sys

stack = []
answer = []
flag = True

n = int(sys.stdin.readline())
now = 1

for _ in range(n):
    num = int(sys.stdin.readline())

    # Push
    while now <= num:
        stack.append(now)
        answer.append('+')
        now += 1
    
    # Pop
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    
    # Impossible
    else:
        flag = False

if flag == False:
    print('NO')
else:
    for i in answer:
        print(i)