h, b, c, s = map(int, input().split())
'''
h = Hz
b = 비트수
c = 채널 개수
s = 초
'''
result = h*b*c*s/8/1024/1024
print(format(result,".1f"),'MB',end=' ')
