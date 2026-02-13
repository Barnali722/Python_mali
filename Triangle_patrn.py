n = int(input("Enter a number: "))
i = n- 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= n - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1