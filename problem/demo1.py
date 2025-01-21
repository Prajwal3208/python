def fib(n):
    if n <= 1:
        return n
    elif n>=2:
        return fib(n-1)+fib(n-2)    
n = 5
print(fib(n))