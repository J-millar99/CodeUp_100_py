n = int(input())
d = []
l = []
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        d.append(i)
for j in d:
    for i in range(1,j+1):
        if j % i == 0:
            cnt +=1
    if cnt == 2:
        l.append(i)
    cnt = 0

if len(l) == 2:
    if l[0] * l[1] == n:
        print(l[0],l[1],sep=' ')
    else:
        print("wrong number")
else:
    print("wrong number")