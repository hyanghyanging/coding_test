import sys
import heapq
'''
최대 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙
우선순위 큐를 이용하는데, 우선순위 큐는 오름차순으로 정렬됨
즉, 3,5,7,1 을 입력하면 우선순위 큐에서는 1,3,5,7 순으로 정렬됨

'''
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    # x가 0이면 배열에서 가장 큰 값 출력
    if x == 0:
        if heap:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    
    # x가 0이 아니라면 배열에 x 푸쉬
    else:
        heapq.heappush(heap, -1 * x)
