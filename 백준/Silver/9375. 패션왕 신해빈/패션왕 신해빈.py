import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cloth = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, type = sys.stdin.readline().split()
        if type in cloth:
            cloth[type].append(name)
        else:
            cloth[type] = [name]
    cnt = 1

    for x in cloth:
        cnt *= (len(cloth[x])+1)

    print(cnt-1)