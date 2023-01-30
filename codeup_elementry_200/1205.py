a, b = map(int, input().split())

c = max(a+b,b+a,a-b,b-a,a*b,b*a,a/b,b/a,a**b,b**a)

print("%.6f" %c)