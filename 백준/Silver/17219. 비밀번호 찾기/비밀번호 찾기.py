import sys

n, m = map(int, sys.stdin.readline().split())
id_pw = {}

for _ in range(n):
    email, pw = map(str, sys.stdin.readline().split())
    id_pw[email] = pw

for _ in range(m):
    address = str(sys.stdin.readline().strip())
    print(id_pw[address])