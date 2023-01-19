gd, cs, nm = input().split()

cs = int(cs)
nm = int(nm)

if cs >= 10:
    cs = str(cs)
else:
    cs = '0'+str(cs)

if 0 <= nm < 10: #번호 한자리
    nm = '00' + str(nm)
elif 10 <= nm < 100: #번호 두자리
    nm = '0' + str(nm)
else:
    nm = str(nm)

result = gd + cs + nm

print(result)