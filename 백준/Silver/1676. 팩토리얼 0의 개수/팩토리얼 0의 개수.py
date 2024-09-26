import sys

n = int(sys.stdin.readline().strip())

fact = 1
for i in range(n):
    fact *= (i+1)

num_list = list(str(fact))
num_list.reverse()

num = 0
for i in range(len(num_list)):
    if int(num_list[i]) == 0:
        num += 1
    else:
        break

print(num)