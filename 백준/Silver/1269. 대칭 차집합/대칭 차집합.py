num_a , num_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a_b = len(set.difference(a,b))
b_a = len(set.difference(b,a))

print(a_b + b_a)