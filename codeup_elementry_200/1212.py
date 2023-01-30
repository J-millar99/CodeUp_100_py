a,b,c = map(int, input().split())

d = [a,b,c]
f = max(d)
d.remove(max(d))

if f < (d[0] + d[1]):
    print("yes")
else:
    print("no")