n = int(input())    #n은 홀수

for i in range(n//2+1): #공백 개수
    print(" "*(n//2-i),end='')
    print("*"*(i*2+1))