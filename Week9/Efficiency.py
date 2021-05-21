# Mesauring Efficiency

def fib(n):
    if n == 0 or n == 1:
        return n 
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    """
    >>> fib = count(fib)
    >>> fib(5)
    5
    >>> fib.call_count
    15
    """
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

# Memoization

def memo(f):
    """Remember the results that have been computed before.
    >>> fib = memo(fib)
    >>> fib(30)
    832040
    """
    cache = {}  #keys are arguments that map to return values.
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized #same behavior as f, if f is a pure function

# Exponentiation

def exp(b, n):   #take Liner time
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def exp_fast(b, n):   #take Logarithmic time
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

def square(x):
    return x*x

# Orders of Growth

def overlap(a, b):   #take Quadratic time
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count 

def fib(n):   #take Exponential time
    if n == 0 or n == 1:
        return n 
    else:
        return fib(n-2) + fib(n-1)

# Space

def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
