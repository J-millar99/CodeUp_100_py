n = int(input())
d = list(map(int,input().split()))

for i in range(n):
    for j in d:
        print(j,end=' ')
    print("")
    a = d.pop(0)
    d.append(a)