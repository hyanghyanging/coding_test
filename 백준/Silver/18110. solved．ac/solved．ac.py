import sys

n = int(sys.stdin.readline())
opinion = [int(sys.stdin.readline()) for _ in range(n)]

def round_1(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)


if len(opinion) == 0:
    print(0)
else:
    opinion.sort()
    trim = round_1(len(opinion) * 0.15)

    if trim > 0:
        trimmed_opinion = opinion[trim : n-trim]
    else:
        trimmed_opinion = opinion[:]
    print(round_1(sum(trimmed_opinion) / len(trimmed_opinion)))
