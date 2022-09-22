n = int(input())

if n > 0 and n % 2 == 0:
    print('C')
elif n > 0:
    print('D')
elif n < 0 and n % 2 == 0:
    print('A')
else:
    print('B')