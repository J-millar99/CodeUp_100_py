height, weight = map(float, input().split())

std = (height - 100) * 0.9
fat = (weight - std) * 100 / std

if fat > 20:
    print("비만")
elif 10 < fat <= 20:
    print("과체중")
else:
    print("정상")