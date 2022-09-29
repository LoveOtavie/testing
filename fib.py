def fib(n, preVal={}):
    if n == 2 or n == 1:
        return 1
    if n in preVal:
        return preVal[n]
    else:
        preVal[n] = fib(n-1, preVal) + fib(n-2, preVal)
        return preVal[n]


print(fib(140))
