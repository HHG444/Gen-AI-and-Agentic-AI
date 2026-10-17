def fib(n):
    """print a fibonacci series"""
    a,b = 0,1
    while a<n:
        print(a,end=":")
        a,b=b,a+b
    print()
fib(10)