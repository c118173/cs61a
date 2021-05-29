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


def nats():
    """A generator that yields all natural numbers.
    """
    curr = 0
    while True:
        curr += 1
        yield curr

def create_skip(n, gen):
    if n == 1:
        yield from gen
    curr, skip = 0, 1
    for elem in gen:
        if skip == n:
            skip = 1
        else:
            curr = curr + elem
            skip = skip + 1
            yield curr

def perfect_ngen(n):
    """
    >>> two_gen = perfect_ngen(2)
    >>> next(two_gen)
    1
    >>> next(two_gen)
    4
    >>> next(two_gen)
    9
    """
    gen = create_skip(n, nats())
    while n > 1:
        n = n - 1
        gen = create_skip(n, gen)
    return gen


def close(n, smallest=10, d=10):
    """A sequence is near-increasing if each element but the last two is smaller than all elements following its subsequent element.
    Return the longest sequence of near-increasing digits in n.
    >>> close(123)
    123
    >>> close(153)
    153
    >>> close(11111111)
    11
    >>> close(985357)
    557
    >>> close(14735476)
    143576
    >>> close(45671)
    4567
    """
    # 1) find close(n//10)
    # 2) use n%10 and everything before it forms a near-increasing sequence
    # 3) return whichever is longer
    if n == 0:
        return 0
    no = close(n//10, smallest, d)  #ignore n%10
    if smallest > n % 10:
        yes = close(n//10, min(smallest, d), n%10) * 10 + n % 10  #take n%10
        return max(yes, no)
    return no


def everything(n):
    """Yield every number within n.
    """
    if n == 0:
        return 0
    else:
        for rest in everything(n//10):
            yield rest
            yield 10*rest + n%10

def increasing(n, smallest=10):
    """Return the largest sequence od digits within n that is increasing.
    >>> increasing(87247861)
    2478
    >>> increasing(367456751)
    34567
    """
    if n == 0:
        return 0
    elif n%10 < smallest:
        no = increasing(n//10, smallest)
        yes = increasing(n//10, min(n%10, smallest)) * 10 + n % 10
        return max(no, yes)
    else:
        return increasing(n//10, smallest)


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


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


def order(redwood):
    """Return a list containing a valid plucking order for the labels of t.
    A plucking order contains all labels of t, and the label for each node of t appears after the labels of all its descendant nodes.
    """
    plucking_order = []
    for b in redwood.branches:
        plucking_order.extend(order(b))
    return plucking_order + [redwood.label]


def pluck(pine):
    """Return a function that returns whether a plucking order is valid for a number tree t when called repeatedly on elements of a plucking order.
    """
    def plucker(k):
        def pluck_one_leaf(cyprus):
            """Return a copy of cyprus without leaf k and check that k is a 
            leaf label, not an interior node label.
            """
            # Assuming cyprus is not a leaf itself
            if cyprus.label == k:
                return 'Hey, not valid!'
            plucked_branches = []
            for b in cyprus.branches:
                skip_this_leaf = b.is_leaf() and b.label == k
                if not skip_this_leaf:
                    plucked_branches_or_error = pluck_one_leaf(b)
                    if isinstance(plucked_branches_or_error, str):
                        return plucked_branches_or_error
                    else:
                        plucked_branches.append(plucked_branches_or_error)
            return Tree(cyprus.label, plucked_branches)

        nonlocal pine
        if pine.is_leaf():
            assert k == pine.label, 'all k must appear in pine'
            return 'success!'
        pine = pluck_one_leaf(pine)
        if isinstance(pine, str): #if cause trouble
            return pine
        else:
            return plucker

    return plucker


def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    """
    if key == k.label:
        yield lambda v: v.label
    for i in range(len(k.branches)):
        for lookup in lookups(k.branches[i], key):
            yield new_lookup(i, lookup)

def new_lookup(i, f): #assuming f is a lookup function for a branches of v
    def g(v):
        return f(v.branches[i])
    return g
