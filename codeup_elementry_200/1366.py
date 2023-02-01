n = int(input())

lst = []

for _ in range(n):
    lst.append([])

for i in range(n):
    for _ in range(n):
        lst[i].append('0') #2차원 배열을 '0'기호로 초기화

for i in range(n):  #테두리 작업
    lst[0][i] = '*'
    lst[i][0] = '*'
    lst[n-1][i] = '*'
    lst[i][n-1] = '*'
for i in range(n):
    lst[(n//2)][i] = '*'
    lst[i][(n//2)] = '*'

for i in range(1,n):
    lst[i][i] = '*'
    lst[i][n-1-i] = '*'



for i in range(n):
    for j in range(n):
        if lst[i][j] == '0':
            print(" ",end='')
        else:
            print(lst[i][j],end='')
    print("\n",end='')
