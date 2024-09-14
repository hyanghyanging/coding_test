import sys

string = str(sys.stdin.readline().strip())
cnt = set()  # 서로 다른 부분 문자열을 set에 저장

for i in range(len(string)):
    for j in range(i,len(string)):
        cnt.add(string[i:j+1])  # i번째부터 j번째까지의 문자열을 set에 추가

print(len(cnt))