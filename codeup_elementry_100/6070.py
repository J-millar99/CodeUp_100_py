month = int(input())

if month // 3 == 0 or month // 3 == 4:
    print('winter')

elif month // 3 == 1:
    print('spring')

elif month // 3 == 2:
    print('summer')

else:
    print('fall')