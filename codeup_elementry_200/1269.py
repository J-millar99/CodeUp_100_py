a,b,c,n = map(int, input().split())
while(n>1):
    a = (a * b + c)
    n -=1

print(a)