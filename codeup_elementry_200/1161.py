n1, n2 = map(int, input().split())

if n1 % 2 == 0:
    print('짝수+',end='')
else:
    print("홀수+",end='')

if n2 % 2 == 0:
    print('짝수=',end='')
else:
    print("홀수=",end='')

if (n1 + n2) % 2 == 0:
    print("짝수")
else:
    print("홀수")