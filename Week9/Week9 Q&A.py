# Q&A old Mid-term

def stable(s, k, n):
    """Return whether all paris of elements of S within distance K differ by at most N.
    """
    for i in range(len(s)):
        near = range(max(0, i-k), k)
        if any([abs(s[i]-s[j]) > n for j in near]):
            return False
    return True


def is_power(base, s):
    """Return whether s is a power of base.
    >>> is_power(5, 625)
    True
    >>> is_power(5, 1)
    True
    >>> is_power(5, 15)
    False
    >>> is_power(3, 10)
    False
    >>> is_power(2, 0)
    False
    """
    assert base > 0 and s >= 0
    assert type(base) is int and type(s) is int
    if s == 1:
        return True
    elif s % base != 0 or s == 0 or base > s:
        return False
    else:
        return is_power(base, s//base)


def power(n, k):
    """Yield all powers of K whose digits appear in order in n.
    >>> sorted(powers(12345, 5))
    [1, 5, 25, 125]
    >>> sorted(powers(2493, 3))
    [3, 9, 243]
    >>> sorted(powers(164352, 2))
    [1, 2, 4, 16, 32, 64]
    """
    def build(seed):
        """Yield all non-negative integers whose digits appear in order in seed.
        0 is yielded because 0 has no digits, so all its digits are in seed.
        """
        if seed == 0:
            yield 0
        else:
            for x in build(seed // 10): #assume we can have all the possibility of seed//10
                yield x
                yield 10 * x + seed % 10 #combine seed//10 with seed%10

    yield from filter(curry2(is_power)(k), build(n)) #is_power call k and every element in build(n)


def reverse_other(t):
    blabel = [b.label for b in t.branches]
    for i in range(len(t.branches)):
        t.branches[i].label = blabel[-i-1]
        for grandchild in t.branches[i].branches:
            reverse_other(grandchild)


def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.
    """

    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        replace(s.rest, t.rest, i-1, j-1)
    else:  # i = 1
        for k in range(j - i): #remove elements at index 1
            s.rest = s.rest.rest
        end = t
        while end.rest is not Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest


class Link:

    empty = ()   # empty tuple
    
    def __init__(self,first,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest

    def __repr__(self):    # represent
        if self.rest is Link.empty():
            return 'Link(' + repr(self.first) + ')'
        return 'Link(' + repr(self.first) + ', ' + repr(self.rest) + ')'

    def __str__(self):    # print
        s = '<'
        while self.rest is not Link.empty:
            s = s + str(self.first) + ', '
            self = self.rest
        return s + str(self.first) + '>'
