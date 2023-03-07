n = int(input())
d = list(map(int, input().split()))
for j in range(1,n+1):
    print("%d: " %j,end='')
    a = d.pop(j-1)
    for i in d:
        if a > i:
            print("> ",end='')
        elif a < i:
            print("< ",end='')
        else:
            print("= ",end='')
    d.insert(j-1,a)
    print("")