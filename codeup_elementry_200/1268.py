n = int(input())
sum = 0
list = list(map(int, input().split()))
for i in range(n):
    if list[i] % 2 != 0:
        sum += 1
print(sum)