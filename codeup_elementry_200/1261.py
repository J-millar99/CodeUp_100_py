list = list(map(int, input().split()))
a=0
for i in list:
    if i%5==0:
        a = i
        break
    
print(a)