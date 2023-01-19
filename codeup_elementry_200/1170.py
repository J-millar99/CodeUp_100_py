gd, cs, nm = input().split()

nm = int(nm)

if nm >= 10:
    result = gd + cs + str(nm)
else:
    result = gd + cs + '0' + str(nm)
    
print(result)