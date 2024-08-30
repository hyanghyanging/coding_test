import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

# 이분 탐색으로 풀기
def binary_search(k):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == k:
            return 1
        if a[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in b:
    print(binary_search(i))