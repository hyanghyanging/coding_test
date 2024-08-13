'''
1. input() vs sys.stdin.readline()
input() : prompt message 출력, 개행 문제 삭제 후 리턴 -> 느림
sys.stdin.readline() : prompt message 출력 X, 개행 문자 포함 값 리턴 -> 빠름

2. 소수 판별법
에라토스테네스의 체 : 모든 소수를 찾아내기 위해 '합성수'를 제거하는 방식
시간복잡도 : O(Nlog(logN))
'''

import sys

m, n = map(int, sys.stdin.readline().split())

is_prime = [False, False] + [True] * (n + 1)   # 리스트 초기화
primes = []

for i in range(2, n+1):
    if is_prime[i]:    # is_prime이 True이면 primes 리스트에 추가
        primes.append(i)
        for j in range(i*2, n+1, i):  # 합성수인 경우 is_prime을 False로 변환
            is_prime[j] = False

for p in primes:
    if p >= m:
        print(p)
