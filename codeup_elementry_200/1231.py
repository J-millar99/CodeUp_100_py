exprs = input()
len = len(exprs)
opt = 0
val = 0
result = 0
for i in range(len):
    if exprs[i] == '+':
        opt = 1 #사칙 연산의 종류 파악
        val = i #연산 기호의 위치 파악
        break
    elif exprs[i] == '-':
        opt = 2
        val = i
        break
    elif exprs[i] == '*':
        opt = 3
        val = i
        break
    elif exprs[i] == '/':
        opt = 4
        val = i
        break
        
if opt == 1:
    result = int(exprs[:i]) + int(exprs[i+1:len])
    print(result)
elif opt == 2:
    result = int(exprs[:i]) - int(exprs[i+1:len])
    print(result)
elif opt == 3:
    result = int(exprs[:i]) * int(exprs[i+1:len])
    print(result)
elif opt == 4:
    result = int(exprs[:i]) / int(exprs[i+1:len])
    print("%.2f" % result)

