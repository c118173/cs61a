# Handling Exceptions

try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

def invert(x):
    y = 1/x
    print('Never print if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled', e)
        return 0

# Example

from operator import mul, pow, add, truediv
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    #for x in s:
    #    initial = f(initial, x)
    #return initial

    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
