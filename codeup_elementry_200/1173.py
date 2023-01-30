hur, min = map(int, input().split())


total = min + (hur * 60) - 30

if total >= 0:
    hur = total // 60 
    min = total % 60
else:
    #total < 0
    hur = 23
    min = total + 60

print(hur, min)