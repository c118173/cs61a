def height(t):
    """ Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1+max([height(b) for b in branches(t)])


def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t)+max([max_path_sum(b) for b in branches(t)])


def square_tree(t):
    """ Return a tree with the square of every element in t"""
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        lst = [square_tree(b) for b in branches(t)]
        return tree(label(t)**2,lst)


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path=find_path(b,x)
        if path:
            return [label(tree)]+path   # Mind the ORDER!


def prune_binary(t,nums):
    """
    >>> t = tree('1',[tree('0',[tree('0'), tree('1')]),tree('1',[tree('0')])])
    >>> new_t = print_tree(prune_binary(t, ['01', '110', '100']))
     1
      0
       0
      1
       0
    """

    if is_leaf(t):
        if any([label(t)==n for n in nums]):
            return t
        return None
    else:
        next_valid_nums= [n[1:] for n in nums if n[0]==label(t)]
        new_branches=[]
        for b in branches(t):
            pruned_branch=prune_binary(b,next_valid_nums)
            if pruned_branch is not None:
                new_branches=new_branches+[pruned_branch]
        if not new_branches:
            return None
        return tree(label(t),new_branches)



# Tree ADT

def tree(label,branches=[]):
    """ Construct a tree with the given label value and a list of branches."""

    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [label]+list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type (tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def print_tree(tree,indent=0):
    """ Print a representation of this tree in which each node is indented
    by two spaces times its depth from the root."""

    print(' '*indent,label(tree))
    for b in branches(tree):
        print_tree(b,indent+1)
