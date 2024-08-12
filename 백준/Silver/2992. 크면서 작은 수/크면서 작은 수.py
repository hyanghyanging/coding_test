from itertools import permutations  # 순열

x = int(input())
num_list = [i for i in str(x)]
num = []

for j in permutations(num_list, len(num_list)):
    num_candidate = int(''.join(j))     # 후보 리스트 생성
    if num_candidate > x:               # 조건을 만족하는 후보는 num 리스트에 추가
        num.append(num_candidate)

num.sort()  # 정렬

if num:
    print(num[0])  # 크면서 작은 수 출력
else:
    print(0)

