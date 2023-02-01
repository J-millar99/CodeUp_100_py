n, m = map(int, input().split())

lst = []

for _ in range(m):
    lst.append([])
for i in range(m):
    for _ in range(n):
        lst[i].append('0') #2차원 배열을 '0'기호로 초기화
        
for i in range(n):
    lst[0][i] = '-'
    lst[m-1][i] = '-'

for i in range(m):
    lst[i][0] = '|'
    lst[i][n-1] = '|'

lst[0][0] = '+'
lst[m-1][n-1] = '+'
lst[0][n-1] = '+'
lst[m-1][0] = '+'

for i in range(m):
    for j in range(n):
        if lst[i][j] == '0':
            print(" ",end='')
        else:
            print(lst[i][j],end='')
    print("\n",end='')