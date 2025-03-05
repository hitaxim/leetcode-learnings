def rotating_factorial(n):
    if n <= 2:
        return n
    if n <= 4:
        return n + 3

    if n % 4 == 0:
        return n + 1
    elif n % 4 == 3:
        return n - 1
    else:
        return n + 2
