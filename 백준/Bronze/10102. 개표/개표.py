import sys
v = int(sys.stdin.readline())
vote = str(sys.stdin.readline())
A, B = 0, 0

for i in range(v):
    if vote[i] == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')
