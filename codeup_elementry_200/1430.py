import sys
print = sys.stdout.write
n = sys.stdin.readline().rstrip()
nd = list(sys.stdin.readline().rstrip().split())
m = sys.stdin.readline().rstrip()
md = list(sys.stdin.readline().rstrip().split())

for i in md:
    if i in nd:
        print("1 ")
    else:
        print("0 ")