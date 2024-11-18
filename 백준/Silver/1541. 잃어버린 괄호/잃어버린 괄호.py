import sys

'''
1. '-' 연산 기준으로 split
2. + 연산
3. num 리스트에서 첫번째 숫자에서 차례대로 빼기
'''
n = sys.stdin.readline().strip().split('-')
num = []

for i in n:
    sum = 0
    for j in i.split('+'):
        sum += int(j)
    num.append(sum)

s = num[0]
for j in range(1, len(num)):
    s -= num[j]
print(s)