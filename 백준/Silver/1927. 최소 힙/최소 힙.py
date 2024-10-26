import sys
import heapq
'''
최소 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙

'''
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    # x가 0이면 배열에서 가장 작은 값 출력
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    
    # x가 0이 아니라면 배열에 x 푸쉬
    else:
        heapq.heappush(heap, x)
