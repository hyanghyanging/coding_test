import sys

n, m = map(int, sys.stdin.readline().split())

listen_names = [str(sys.stdin.readline().strip()) for _ in range(n)]
look_names = [str(sys.stdin.readline().strip()) for _ in range(m)]
name = sorted(list(set(listen_names) & set(look_names)))

print(len(name))
for i in name:
    print(i)