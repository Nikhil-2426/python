def lucas(n):
    if n==0:
        return 0
    if n<=2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)+lucas(n-3)

number=30

for i in range(number):
    print(lucas(i),end=' ')

