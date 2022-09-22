n = int(input())
a = input().split()

a_list = []
for _ in range(23):
    a_list.append(0)

for i in range(n):
    a_list[int(a[i])-1] += 1

for i in range(23):
    print(a_list[i],end=' ')