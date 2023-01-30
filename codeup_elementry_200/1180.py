n = int(input())

n = (n % 10 * 10) + (n // 10)
n *=2
n %= 100
 
print(n)
if (n<=50):
    print("GOOD")
else:

    print("OH MY GOD")