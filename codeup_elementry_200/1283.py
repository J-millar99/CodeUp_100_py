a = int(input())
b = int(input())
d = list(map(int, input().split()))

vaf = a
vaf = float(vaf)

for i in d:
    vaf += vaf*i/100
result = vaf - a

print(round(result))
if result > 0.5:
    print("good")
elif -0.5 < result < 0.5:
    print("same")
else:
    print("bad")