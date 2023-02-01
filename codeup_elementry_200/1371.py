n = int(input())

for i in range(n):
    print(" "*(n-1-i),"*",sep='',end='') 
    print(" "*(2*i),"*",sep='')

for i in range(n-1, -1, -1):
    print(" "*(n-1-i),"*",sep='',end='') 
    print(" "*(2*i),"*",sep='')