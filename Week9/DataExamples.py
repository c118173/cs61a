# Object

class Worker:
    greeting = 'Sir'

    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'


# Iterables & Iterators

def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.
    """
    min_abs = min(map(abs, s))
    #return [i or i in range(len(s)) if abs(s[i]) == min_abs]
    f = lambda i: abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, -3, -2, -3, 2, -4])
    1
    """
    #return max([s[i] + s[i+1] for i in range(len(s)-1)])
    return max([a + b for a, b in list(zip(s[:-1], s[1:]))])

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.
    """
    #return {d: [x for x in s if x%10==d] for d in range(10) if any([x%10==d for x in s])}
    last_digits = [x % 10 for x in s]
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}

def all_have_an_equal(s):
    """Does every element equal some other element in s?
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    #return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    #return all([sum([1 for y in s if y == x]) > 1 for x in s])
    return min([s.count(x) for x in s]) > 1


# Linked List

def ordered(s, key=lambda x: x):
    """Is Link s ordered?
    >>> ordered(Link(1, Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(-3, Link(4))), key = abs)
    """
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)

def merge(s, t):
    """Return a sorted Link with the elements of sorted s & t.
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1. Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    """Return a sorted Link with the elements of sorted s & t.
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t. first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t


class Link:

    empty = ()   # empty tuple
    
    def __init__(self, first, rest=empty):
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