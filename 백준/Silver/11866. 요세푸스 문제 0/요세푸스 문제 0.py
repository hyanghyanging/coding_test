import sys , queue

N, K = map(int, sys.stdin.readline().split())
index = 0
result = []
array = [i for i in range(1, N+1)]

while len(array) != 0:
    index += (K-1)    # K번째 숫자 pop 되니까 K-1 해줘야 함
    index = index % len(array)  # 1바퀴 이상 돌 경우 나머지만 활용하면 됨
    result.append(array.pop(index))

print('<' + str(result)[1:-1] + '>')