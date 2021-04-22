def count_stair_ways(n):
    if n==1 or n==0:
        return 1
    if n<0:
        return 0
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n,k):
    """
    >>> count_k(3,3)
    4
    >>> count_k(4,4)
    8
    >>> count_k(10,3)
    274
    >>> count_k(300,1)
    1
    """
    if n<0:
        return 0 
    elif n==0:
        return 1
    else:
        total=0
        i=1
        while i<=k:
            total += count_k(n-i,k)
            i += 1
        return total

def even_weighted(s):
    """
    >>> x=[1,2,3,4,5,6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*s[i] for i in range(len(s)) if i % 2 == 0]

def max_product(s):
    """ Return the maximum product that can be formed using non-consecutive elements of s.

    >>> max_product([10,3,1,9,2])
    90
    >>> max_product([5,10,5,10,5])
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    elif len(s)==1:
        return s[0]
    else:
        return max(max_product(s[1:]),s[0]*max_product(s[2:]))

def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n//10 == 0:
        return True
    return ((n//10)%10) < (n%10) and ((n//10)%10) < ((n//100)%10) and check_hole_number(n//100) 

def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(3241968)
    False
    >>> check_mountain_number(2345986)
    True
    """
    def helper(x, is_increasing):
        if x//10==0:
            return True
        if is_increasing and (x%10)<((x//10)%10):
            return helper(x//10,True)
        return (x%10)>((x//10)%10) and helper(x//10,False) # True and True
    return helper(n,True)
