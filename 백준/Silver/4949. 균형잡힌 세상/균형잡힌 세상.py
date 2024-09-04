while True:
    ps = input()
    check = ''
    answer = 'yes'

    if ps == '.':   # . 나올때까지 반복
        break
    for s in ps:
        if s not in '()[]':
            continue
        else:
            check += s

    for _ in range(len(check)//2+1):
        check = check.replace('()', '')  # 올바른 괄호 문자열이면 제거
        check = check.replace('[]', '')  # 올바른 괄호 문자열이면 제거
    
    if len(check):
        print('no')   # check 안에 문자열이 존재하면 no, 
    else:
        print('yes')  # 존재하지 않으면 모두 올바른 문자열로 취급하여 yes 출력