a, b, c= map(int, input().split())

d = a if (a <= b) else b
e = c if (c <= b) else b

print(d if (d<=e) else e)