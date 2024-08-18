import sys
from collections import Counter


n = int(sys.stdin.readline())
value=[int(sys.stdin.readline()) for i in range(n)]


value.sort()

# 산술평균
print(round(sum(value)/n))  

# 중앙값
print(value[n//2])          

# 최빈값
freq = Counter(value).most_common()     # most_common : 데이터의 개수가 많은 순으로 정렬
max_freq = freq[0][1]
modes = [num for num, cnt in freq if cnt == max_freq]

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(value[-1] - value[0])