age = int(input())

year = 2012 - age + 1

if year >= 2000:
    print(year%100, 3)
else:
    print(year%100, 1)