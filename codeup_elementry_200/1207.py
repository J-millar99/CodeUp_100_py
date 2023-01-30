r1,r2,r3,r4 = map(int, input().split())

sum = r1+r2+r3+r4

if sum ==0:
    print("모")
elif sum ==1:
    print("도")
elif sum ==2:
    print("개")
elif sum ==3:
    print("걸")
else: #sum = 5
    print("윷")