import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    people = [x for x in range(1, n+1)]  
    for _ in range(k):
        for i in range(1, n): 
            people[i] += people[i-1] 
    print(people[n-1])