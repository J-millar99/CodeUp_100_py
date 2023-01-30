lotto =  list(map(int, input().split()))

list =  list(map(int, input().split()))

cnt = 0
bns = 0

for i in range(6):
    for j in range(6):
        if list[j] == lotto[i]:
            cnt +=1
for k in range(6):
    if list[k] == lotto[6]:
        bns +=1
    
if cnt == 5 and bns == 1:
    print("2")
elif cnt == 6:
    print("1")
elif cnt == 5:
    print("3")
elif cnt == 4:
    print("4")
elif cnt == 3:
    print("5")
elif cnt <= 2:
    print("0")