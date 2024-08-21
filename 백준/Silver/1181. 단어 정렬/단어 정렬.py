import sys

n = int(sys.stdin.readline())
words = [str(sys.stdin.readline().strip()) for i in range(n)]   # strip()으로 개행 문자 제거

words = list(set(words))  # set 으로 중복 제거 -> list 변환

words.sort()          # 문자열을 사전 순으로 정렬
words.sort(key=len)   # key를 사용해 문자열 길이를 기준으로 정렬

for word in words:
    print(word)


