k, h = map(int, input().split())
money = 0

if k % 2 == 0:
    k = k//2 * 10
else: #k가 홀수일 경우
    k = k//2 + 1
    

if h % 2 == 0:
    h = h//2 * 10
else:
    h = h//2 + 1
    
money = money + k + h
print(money)