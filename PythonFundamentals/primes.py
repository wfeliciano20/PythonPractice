for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print('{} equals {} * {}').format(n, x, n/x)
            break
    else:
        print('{} is a prime number.').format(n)
