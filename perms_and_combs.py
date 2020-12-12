def factorial(n):
    return n if n == 1 else n * factorial(n-1)

def C(n, r):
    return (factorial(n))/(factorial(r)*factorial(n-r))

def P(n, r):
    return factorial(n)/factorial(n-r)