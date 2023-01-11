sec = int(input())

min = sec // 60 # 초를 60으로 나눈 몫이 분이 된다
sec%=60         # 그 나머지는 초로 남겨둔다

print(min, sec)