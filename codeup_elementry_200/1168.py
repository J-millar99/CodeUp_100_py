birth, sex = map(int, input().split())
birth = birth // 10000
if sex <= 2: # 1900년대 이후 출생자
    birth = 1900 + birth
    print(2012 - birth + 1)
else: #2000년대 이후 출생자
    birth = 2000 + birth
    print(2012 - birth + 1)