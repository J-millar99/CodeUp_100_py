str1 = input()
str2 = ''
for i in str1:
    i = ord(i)
    if ord('a') <= i <= ord('z'):
        i -= 3
        if i < ord('a'):
            i = i + ord('z') - ord('a') + 1
    str2 += chr(i)
print(str2)