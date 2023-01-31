n = int(input())
i = 0
k = 0
t = 0   #k는 빼는 수, t는 제곱근

while(i**2<n):
    i+=1

i -= 1
k = n - i**2

print(k,i,sep=' ')