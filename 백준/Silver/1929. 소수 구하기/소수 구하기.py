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

for i in range(m, n+1):
    if i == 1:               # 1은 소수가 아님
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:       # i가 합성수일 경우 나누어 떨어짐
            break
    else:
        print(i)