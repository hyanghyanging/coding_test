s = input()   # s : 문자열
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:     # 0->1 또는 1->0 일 경우 cnt += 1
        cnt += 1

print((cnt+1)//2)   # 중복 카운트 제거