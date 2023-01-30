a, b = map(int, input().split())

if a % b == 0:
    x = a // b
    print("%d*%d=%d" %(b,x,b*x))
elif b % a == 0:
    x = b // a
    print("%d*%d=%d" %(a,x,a*x))
else:
    print("none")