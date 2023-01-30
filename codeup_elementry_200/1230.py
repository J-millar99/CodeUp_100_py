hgt = 170

a,b,c = map(int, input().split())

if a > hgt and b > hgt and c > hgt:
    print("PASS")
else:
    print("CRASH",end=' ')
    if a <= hgt:
        print(a)
    elif b <= hgt:
        print(b)
    else:
        print(c)