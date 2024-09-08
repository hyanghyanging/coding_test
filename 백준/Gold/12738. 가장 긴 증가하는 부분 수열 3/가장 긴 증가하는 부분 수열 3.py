import sys
import bisect

a = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
cnt = [array[0]]

for i in range(1, a):
    if cnt[-1] < array[i]:
        cnt.append(array[i])
    else:
        idx = bisect.bisect_left(cnt, array[i])
        cnt[idx] = array[i]

print(len(cnt))