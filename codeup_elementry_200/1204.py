day = int(input())
res = day % 10

if day // 10 == 1:
    print("%dth" %day)
else:
    if res == 1:
        print("%dst" %day)
    elif res == 2:
        print("%dnd" %day)
    elif res == 3:
        print("%drd" %day)
    else:
        print("%dth" %day)