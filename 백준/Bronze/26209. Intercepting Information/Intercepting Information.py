import sys

numbers = list(map(int, sys.stdin.readline().split()))
bit = True

for num in numbers:
    if num in [0, 1]:
        bit = True
    else:
        bit = False
        print("F")
        break

if bit:
    print("S")