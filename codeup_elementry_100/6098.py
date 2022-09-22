
d = [list(map(int, input().split())) for _ in range(10)]

i = 1; j = 1
# (1,1) 시작지점
while True: #첫시작 #1
    if d[i][j] == 0:
        d[i][j] = 9
        if d[i][j+1] == 0: #오른쪽 이동 가능한 경우 무조건 이동
            j += 1
        elif d[i][j+1] == 1 and d[i+1][j] == 0: #오른쪽이 1이고 아래 이동이 가능한경우
            i += 1
        elif d[i][j+1] == 1 and d[i+1][j] == 1: #오른쪽, 아래 모두 벽인 경우
            break
        elif d[i][j+1] == 2:
            d[i][j+1] = 9
            break
        elif d[i+1][j] == 2:
            d[i+1][j] = 9
            break

for a in range(10):
    for b in range(10):
        print(d[a][b],end=' ')
    print()
