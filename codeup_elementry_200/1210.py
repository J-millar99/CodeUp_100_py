n1, n2 = map(int, input().split())

d = [400, 340, 170, 100, 70]

sum = d[n1-1] + d[n2-1]

if sum > 500:
    print("angry")
else:
    print("no angry")
    
