'''
<문제 분석>

line이 짝수일 경우
분자 : 오름차순 / 분모 : 내림차순
line이 홀수일 경우
분자 : 내림차순 / 분모 : 오름차순
'''

x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    a = x
    b = line-x+1
else:
    a = line-x+1
    b = x

print('{}/{}'.format(a, b))
        
