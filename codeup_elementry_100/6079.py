n = int(input())
sum = 0

for i in range(1,n+1):
    if sum < n:
        sum +=i
    else:
        break

print(i-1)