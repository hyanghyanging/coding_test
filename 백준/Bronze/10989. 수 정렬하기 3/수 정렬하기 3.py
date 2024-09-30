import sys

'''
시간초과 문제를 해결하기 위해선 계수정렬을 활용해야 함.
계수정렬
- 최대값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬 수행
- 최대값이 작을수록 정렬에 유리함.
- 시간복잡도: O(N)
'''
n = int(sys.stdin.readline())
# numbers = []
arr = [0] * (10000+1)  # 입력값이 최대 10,000개 주어짐

for _ in range(n):
    arr[int(sys.stdin.readline().strip())] += 1  # 해당하는 입력값의 인덱스 값 증가

for i in range(len(arr)):
    if arr[i] != 0:  # 입력받은 데이터 출력
        for _ in range(arr[i]):
            print(i)
