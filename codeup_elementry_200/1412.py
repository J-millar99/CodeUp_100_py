str = input()
cnt = 0
alpha = 97

for i in range(26):
    cnt = str.count(chr(alpha+i))
    print(chr(alpha+i),":",cnt,sep='')