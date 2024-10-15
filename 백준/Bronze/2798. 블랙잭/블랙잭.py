import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
results = 0

for choices in combinations(cards, 3):
    if sum(choices) <= m:
        results = max(results, sum(choices))
print(results) 