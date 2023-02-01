h, k, d = input().split()

h = int(h)
k = int(k)

if d == 'L':
    for i in range(h):
        print(" "*i,"*"*k,sep='')
else:
    for i in range(h):
        print(" "*(h-i-1),"*"*k,sep='')