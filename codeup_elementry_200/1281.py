a,b = map(int, input().split())
sum = 0
eps = ''
for i in range(a,b+1):
    if i % 2 == 0:
        sum -= i
        eps = eps + '-' + str(i)
    else: 
        sum += i
        eps = eps + '+' + str(i)
eps = eps + '=' + str(sum)
eps = eps.lstrip("+")
print(eps)