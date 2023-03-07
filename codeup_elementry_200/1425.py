n, c = map(int, input().split())

height = list(map(int, input().split()))
height.sort()
a = 0
for i in range(n):
    if ((i != 0 )and (i % c == 0)):
        print()
    print(height[i], end=' ')