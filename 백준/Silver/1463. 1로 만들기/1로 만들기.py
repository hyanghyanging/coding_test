import sys

x = int(sys.stdin.readline().strip())

operation = [0] * (x+1)  # 각 숫자에서의 최소 연산 횟수 저장

for i in range(2, x+1):
    operation[i] = operation[i-1] + 1
    if i % 3 == 0:
        operation[i] = min(operation[i], operation[i//3] +1)
    if i % 2 == 0:
        operation[i] = min(operation[i], operation[i//2] +1)

print(operation[x])