eps = input()
len = len(eps)

total = 0
total = int(total)

for j in range(len):
    if not (47 < ord(eps[j]) < 58):
        total += int(eps[:j])
        break

for i in range(len):
    if eps[i] == '+':
        for j in range(i+1,len):
            if not (47 < ord(eps[j]) < 58): #사칙연산 기호라면
                total += int(eps[i+1:j])
                break
        
    elif eps[i] == '-':
        for j in range(i+1,len):
            if not (47 < ord(eps[j]) < 58):
                total -= int(eps[i+1:j])
                break
        
    elif eps[i] == '*':
        for j in range(i+1,len):
            if not (47 < ord(eps[j]) < 58):
                total *= int(eps[i+1:j])
                total = int(total)
                break
        
    elif eps[i] == '/':
        for j in range(i+1,len):
            if not (47 < ord(eps[j]) < 58):
                total /= int(eps[i+1:j])
                total = int(total)
                break
        
print(total)