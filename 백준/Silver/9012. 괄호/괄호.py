T = int(input())


for i in range(T):
    ps = input()
    ps_list=[]

    for j in ps:
        if j == '(':
            ps_list.append(i)
        else:
            if ps_list:
                ps_list.pop()
            else:
                print("NO")
                break
    else:
        if len(ps_list) == 0:
            print("YES")
        else:
            print("NO")