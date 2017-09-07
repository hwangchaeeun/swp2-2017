n = 0
while n != -1:
    f = 1
    n = int(input('Enter a number: '))
    for i in range(1, n + 1):
        f = f * i
    if n <= -1:
        break
    print(n, '! = ',f)