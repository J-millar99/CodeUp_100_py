str1 = input()
diff = ord('a') - ord('A')
str2 = ''
for i in str1:
    i = ord(i)
    if ord('A') <= i <= ord('Z'): #대문자를 소문자로
        i += diff
        i = chr(i)
        str2 += i
        
    elif ord('a') <= i <= ord('z'): #소문자를 대문자로
        i  -= diff
        i = chr(i)
        str2 += i
    else:
        str2 += chr(i)

print(str2)