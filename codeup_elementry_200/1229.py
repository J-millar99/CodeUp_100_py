height, weight = map(float, input().split())

if height >= 160:
    std = (height - 100) * 0.9
elif 150 <= height < 160:
    std = (height - 150) / 2 + 50
else:
    std = height - 100
fat = (weight - std) * 100 / std

if fat > 20:
    print("비만")
elif 10 < fat <= 20:
    print("과체중")
else:
    print("정상")