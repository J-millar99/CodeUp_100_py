r, g, b = map(int, input().split())

result = r*g*b/8/1024/1024
print(format(result,".2f"),'MB',end=' ')
