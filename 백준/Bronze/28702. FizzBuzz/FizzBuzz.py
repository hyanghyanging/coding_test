import sys

string = [sys.stdin.readline().strip() for i in range(3)]

for i in range(2, -1, -1):
    if string[i].isdigit():   # 숫자 찾기
        answer = int(string[i]) + (3-i)  
        break

if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)