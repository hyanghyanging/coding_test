import sys

N = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
num_list.sort()

for i in num_list:
    print(i)
