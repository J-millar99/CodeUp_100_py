n = int(input())
sum = 0
list = list(map(int, input().split()))
for i in range(n):
    if list[i] % 5 == 0:
        sum += list[i]
print(sum)