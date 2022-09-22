n = input()

o = int(n,16)

for i in range(1,16):
    print('%X'%o,"*",'%X'%i,'=','%X'%(o*i),sep='')