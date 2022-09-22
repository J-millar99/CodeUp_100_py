d = [list(map(int, input().split())) for _ in range(19)]

n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(19):
        if d[x-1][i] ==1:
            d[x-1][i] =0
        else:
            d[x-1][i] = 1
        if d[i][y-1] ==1:
            d[i][y-1] =0
        else:
            d[i][y-1] =1

for i in range(19) :
    for j in range(19) : 
        print(d[i][j], end=' ')
    print()