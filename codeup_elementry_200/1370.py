h, r = map(int, input().split())

while(r>0):
    for i in range(h): # h=3
        print(" "*i,"*",sep='')
        if i == h-1: # i=2
            for j in range(h-2,-1,-1):
                print(" "*j,"*",sep='')
    r -=1