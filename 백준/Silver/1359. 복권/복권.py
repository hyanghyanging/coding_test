import sys
from itertools import combinations

n, m, k = map(int, sys.stdin.readline().split())  
'''
1부터 N까지 수 중 서로 다른 M개의 수. 
정답과 적어도 K개의 수가 같으면 당첨
'''
lottery = [i for i in range(1, n+1)]     # 가능한 숫자 리스트
pick_comb = [*combinations(lottery, m)]  # 모든 숫자 조합

winning = 0

# 당첨 조합 개수
for pick in pick_comb:
    for win_comb in combinations(lottery,m):
        cnt = len(set(pick) & set(win_comb))   # 맟춘 숫자의 개수
        if cnt >= k:                # 적어도 k개의 수가 같은지 확인
            winning += 1

# 전체 조합 개수
total = len(pick_comb)**2

print(winning/total)