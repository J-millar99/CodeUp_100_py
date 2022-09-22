h, w = map(int, input().split())
n = int(input())

list = []
for i in range(h):
    list.append([])
    for _ in range(w):
        list[i].append(0)

for _ in range(n):
    l,d,x,y = map(int, input().split())
    x = x-1
    y = y-1
# d=0 가로 d=1 세로
    list[x][y] = 1
    for k in range(1,l):
        if d == 0:
            list[x][y+k] = 1
        else: # d==1:
            list[x+k][y] = 1
    
for a in range(h):
    for b in range(w):
        print(list[a][b],end= ' ')
    print()
