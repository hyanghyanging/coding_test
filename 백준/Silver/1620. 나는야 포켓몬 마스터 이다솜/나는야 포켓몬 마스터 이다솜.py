import sys

n, m = map(int, sys.stdin.readline().split()) # n: 포켓몬 개수, m: 맞춰야하는 문제의 개수

poketmon_int_key = {}
poketmon_name_key = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    poketmon_int_key[i] = name
    poketmon_name_key[name] = i

for _ in range(m):
    question = sys.stdin.readline().strip()
    if question.isdigit(): # 질문이 숫자인 경우 -> 포켓몬 번호에 해당하는 문자 출력
        print(poketmon_int_key[int(question)-1])
    else:
        print(poketmon_name_key[question]+1) # 문제가 알파벳 -> 포켓몬 번호 출력
    