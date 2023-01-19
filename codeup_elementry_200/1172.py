a, b, c = map(int, input().split())

d = [a,b,c]

list.sort(d)
for i in d:
    print(i,end=' ')