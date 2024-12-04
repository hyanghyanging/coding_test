import sys

k = int(sys.stdin.readline())

result = []
for i in range(1000):
    result.append(1)
for j in range(1000):
    result.append(1000)

print(len(result))
print(*result)