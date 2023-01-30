year, month = map(int, input().split())

if month <= 7 and month % 2 == 1:
    day = 31
elif month >= 8 and month % 2 == 0:
    day = 31
elif month ==2:
    if year % 400 ==0 or (year % 4 ==0 and year % 100 !=0):
        day = 29
    else:
        day = 28
else:
    day = 30

print(day)