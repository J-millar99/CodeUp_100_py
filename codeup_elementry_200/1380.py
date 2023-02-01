k = int(input())

for i in range(1,7):
    for j in range(6,0,-1):
        if i + j == k:
            print(i,j,sep=' ')
