"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(x, y):
    """
    Multiply two numbers.

    Args: 
        x: number
        y: number
    
    Returns:
        product of x * y
    """
    return x * y


def id(x):
    """
    f(x) = x
    """
    return x


def add(x, y):
    """
    f(x, y) = x +y
    """
    return x + y


def neg(x):
    """
    f(x) = -x
    """
    return -x


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    return x < y


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    return x == y


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    if x > y:
        return x
    return y


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2`"
    val = abs(x - y)
    return val < math.e - 2


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    return 1.0/(1.0 + math.e**(-x))


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    return max(0, x)


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def inv(x):
    ":math:`f(x) = 1/x`"
    return x**-1


def log_back(x, y):
    r"If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    return (1/x) * y


def inv_back(x, y):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    return -(1/x**2) * y


def relu_back(x, y):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    return y if x > 0 else 0
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(func, iter):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """
    for i in iter:
        yield func(i)


def zipWith(func):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """
    return lambda list1, list2 : (func(x, y) for x, y in zip(list1, list2))


def reduce(func, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """
    def _reduce(ls, func, start):
        iterator = iter(ls)
        for i in iterator:
            start = func(start, i)
        return start
    
    return lambda ls: _reduce(ls, func, start)


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    negated = map(neg, ls)
    return [i for i in negated]


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    return [i for i in zipWith(add)(ls1, ls2)]


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    return reduce(add, 0)(ls)


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    return reduce(mul, 1)(ls)

chuj = prod([5, 3, 2])
print(chuj)