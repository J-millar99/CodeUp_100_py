n = int(input())
sum = 0
list = list(map(int, input().split()))
for i in range(n):
    sum += list[i]
print(sum)