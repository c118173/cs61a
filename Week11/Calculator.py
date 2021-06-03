# a partial code for the Calculator copied from the John's lecture

from typing import Type
from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.
    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError #end of file error
    val = src.pop()
    if val == 'nil':
        return nil
    elif val not in DELIMITERS: # () ' .
        return val
    elif val == "(":
        return read_tail(src)
    else:
        raise SyntaxError("unexpected token: {0}.format(val")

def read_tail(src):
    """Return the remainder of a list in src, starting before an element or ).
    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest = read_tail(src)
    return Pair(first, rest)

class Pair:
    """A Pair has two instance attributes: first and second.

    For a Pair to be a well-formed list, second is either a well-formed list or nil.
    Some methods only apply to well-formed lists.
    """

    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second, Pair):
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"
    
    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n
    
    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first

    def map(self, fn):
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

def calc_eval(exp):
    """Evaluate a Calculator expression.
    >>> cal_eval(as_scheme_list('+', 2, as_scheme_list))
    """
    if type(exp) in (int, float):
        return simplify(exp)
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return simplify(cal_apply(exp.first, arguments))
    else:
        raise TypeError(str(exp) + ' is not a number or call expression')

def calc_apply(operator, args):
    """Apply the named operator to a list of args.
    >>> calc_apply('+', as_scheme_list(1, 2, 3))
    6
    >>> calc_apply('-', as_scheme_list(10, 1, 2, 3))
    4
    """
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' is an unknown operator')

def simplify(value):
    """Return an int if value is an integer, or value otherwise.
    """
    if isinstance(value, float) and int(value) == value:
        return int(value)
    return value

def reduce(fn, scheme_list, start):
    """Reduce a recursive list of Pair using fn and a start value.
    """
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.second, fn(start, scheme_list.first))

def as_scheme_list(*args):
    """Return a recursive list of Pairs that contains the elements of args.
    >>> as_scheme_list(1, 2, 3)
    Pair(1, Pair(2, Pair(3, nil)))
    """
    if len(args) == 0:
        return nil
    return Pair(args[0], as_scheme_list(*args[1:]))

# Interactive loop

def buffer_input():
    return Buffer(tokenize_lines(InputReader('> ')))

@main  #if __name__ == '__main__':
def read_eval_print_loop():
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(typr(err).__name__ _ ':', err)
        except (KeyboardInterrupt, EOFError): #<Control>--D, etc.
            print('Calculation completed.')
            return