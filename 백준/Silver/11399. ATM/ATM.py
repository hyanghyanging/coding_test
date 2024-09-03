import sys

N = int(sys.stdin.readline().strip())
P_list = list(map(int, sys.stdin.readline().split()))

P_list.sort()
withdraw_time = []
time_sum = 0

for i in range(N):
    time_sum += int(P_list[i])
    withdraw_time.append(time_sum)

print(sum(withdraw_time))