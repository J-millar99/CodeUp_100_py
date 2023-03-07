n = int(input())
d = []
b = 0
for i in range(1,n+1):
    d.append(i)

for j in range(n-1):
    a = int(input())
    d.remove(a)

print(d[0])