n = int(input())
score_list = []
d = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    score_list.append(score)
    d.append(name)
    d.append(score)

score_list.sort()
a = score_list[n-3]
b = d.index(a)
c = d[b-1]
print(c)