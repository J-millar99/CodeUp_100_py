n = int(input())

list = list(map(int, input().split()))
max = list[0]
for i in range(n):
    if max < list[i]:
        max = list[i]
        
print(max)