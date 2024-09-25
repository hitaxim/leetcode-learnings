def minSum(a, n):
    # sorted the elements
    a = sorted(a)
    num1, num2 = 0, 0
     
    for i in range(n):
        if i % 2 == 0:
            num1 = num1 * 10 + a[i]
        else:
            num2 = num2 * 10 + a[i]
     
    return num2 + num1     
     
