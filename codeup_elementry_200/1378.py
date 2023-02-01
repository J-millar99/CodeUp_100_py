n = int(input())
sum = 0
for i in range(n):
    for j in range(n):
        sum = sum + n-j
    n -=1
print(sum)