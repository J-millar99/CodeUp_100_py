n = int(input())

for i in range(1,n+1):
    r = i % 10
    if r == 0: # 10, 20 case
        print(i,end=' ')
    elif r % 3 == 0: #나머지가 3, 6, 9 case
        print('X',end=' ')
    else:
        print(i,end=' ')