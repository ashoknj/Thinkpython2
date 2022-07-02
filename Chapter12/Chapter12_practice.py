from structshape import structshape

#########        Tuples
"""
Tuples are simialr to list but they are immutable. created bt ()   bracket, we can even crrate without ()

    To create a tuple with a single element, you have to include a final comma:
    >>> t1 = 'a',
    >>> type(t1)
    <class 'tuple'>
IMP:    A value in parentheses is not a tuple:
    >>> t2 = ('a')
    >>> type(t2)
    <class 'str'>

    Another way to create a tuple is the built-in function tuple. With no argument, it creates
    an empty tuple:
    >>> t = tuple()
    >>> t
    ()

    If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of
    the sequence:
    >>> t = tuple('lupins')
    >>> t
    ('l', 'u', 'p', 'i', 'n', 's')

    Most list operators also work on tuples. The bracket operator indexes an element like t[0], t[1:3]

IMP  But if you try to modify one of the elements of the tuple, you get an error:
    >>> t[0] = 'A'
    TypeError: object doesn't support item assignment

#### Relational operator

    The relational operators work with tuples and other sequences; Python starts by comparing
    the first element from each sequence. If they are equal, it goes on to the next elements, and
    so on, until it finds elements that differ. Subsequent elements are not considered (even if
    they are really big).
    >>> (0, 1, 2) < (0, 3, 4)
    True
    >>> (0, 1, 2000000) < (0, 3, 4)
    True

####  tuple assignments
    tuple assignment is more elegant:
    >>> a, b = b, a

    The left side is a tuple of variables; the right side is a tuple of expressions. Each value is
    assigned to its respective variable. All the expressions on the right side are evaluated
    before any of the assignments.

    More generally, the right side can be any kind of sequence (string, list or tuple). For
    example, to split an email address into a user name and a domain, you could write:
    >>> addr = 'monty@python.org'
    >>> uname, domain = addr.split('@')
    The return value from split is a list with two elements; the first element is assigned to
    uname, the second to domain:
    >>> uname
    'monty'
    >>> domain
    'python.org'

###   Function return tuple
    def min_max(t):
    return min(t), max(t)
    max and min are built-in functions that find the largest and smallest elements of a
    sequence. min_max computes both and returns a tuple of two values.

#### Variable-Length Argument Tuples
    Functions can take a variable number of arguments. A parameter name that begins with *
    gathers arguments into a tuple. For example, printall takes any number of arguments
    and prints them:

        def printall(*args):
        print(args)
    The gather parameter can have any name you like, but args is conventional. Here’s how
    the function works:
    >>> printall(1, 2.0, '3')
        (1, 2.0, '3')

    The complement of gather is scatter. If you have a sequence of values and you want to
    pass it to a function as multiple arguments, you can use the * operator. For example,
    divmod takes exactly two arguments; it doesn’t work with a tuple:
        >>> t = (7, 3)
        >>> divmod(t)
        TypeError: divmod expected 2 arguments, got 1

    But if you scatter the tuple, it works:
        >>> divmod(*t)
        (2, 1)

    Many of the built-in functions use variable-length argument tuples. For example, max and
    min can take any number of arguments:
    >>> max(1, 2, 3)
    3
    But sum does not:
    >>> sum(1, 2, 3)
    TypeError: sum expected at most 2 arguments, got 3

### List and Tuples
    zip is a built-in function that takes two or more sequences and returns a list of tuples
    where each tuple contains one element from each sequence.
    >>> s = 'abc'
    >>> t = [0, 1, 2]
    >>> zip(s, t)
    <zip object at 0x7f7d0a9e7c48>

    The result is a zip object that knows how to iterate through the pairs. The most common
    use of zip is in a for loop:
    >>> for pair in zip(s, t):
    ... print(pair)

*   A zip object is a kind of iterator, which is any object that iterates through a sequence.
    Iterators are similar to lists in some ways, but unlike lists, you can’t use an index to select
    an element from an iterator.

If you want to use list operators and methods, you can use a zip object to make a list:
    >>> list(zip(s, t))
    [('a', 0), ('b', 1), ('c', 2)]

    The result is a list of tuples; in this example, each tuple contains a character from the
    string and the corresponding element from the list.

    If the sequences are not the same length, the result has the length of the shorter one:
        >>> list(zip('Anne', 'Elk'))
        [('A', 'E'), ('n', 'l'), ('n', 'k')]

    You can use tuple assignment in a for loop to traverse a list of tuples:
        t = [('a', 0), ('b', 1), ('c', 2)]
        for letter, number in t:
        print(number, letter)
    
    If you combine zip, for and tuple assignment, you get a useful idiom for traversing two
    (or more) sequences at the same time. For example, has_match takes two sequences, t1
    and t2, and returns True if there is an index i such that t1[i] == t2[i]:
        def has_match(t1, t2):
            for x, y in zip(t1, t2):
                if x == y:
                    return True
            return False
    If you need to traverse the elements of a sequence and their indices, you can use the builtin
    function enumerate:
        for index, element in enumerate('abc'):
            print(index, element)
    
    The result from enumerate is an enumerate object, which iterates a sequence of pairs; each
    pair contains an index (starting from 0) and an element from the given sequence.
    In this example, the output is
        0 a
        1 b
        2 c


#### Dictionaries and Tuples
    Dictionaries have a method called items that returns a sequence of tuples, where each
    tuple is a key-value pair:
    >>> d = {'a':0, 'b':1, 'c':2}
    >>> t = d.items()
    >>> t
    dict_items([('c', 2), ('a', 0), ('b', 1)])

   
    Combining dict with zip yields a concise way to create a dictionary:
    >>> d = dict(zip('abc', range(3)))
    >>> d
    {'a': 0, 'c': 2, 'b': 1}

#### Sequences of Sequences


    In many contexts, the different kinds of sequences (strings, lists and tuples) can be used
    interchangeably. So how should you choose one over the others?

    To start with the obvious, strings are more limited than other sequences because the
    elements have to be characters. They are also immutable. If you need the ability to change
    the characters in a string (as opposed to creating a new string), you might want to use a list
    of characters instead.

    Lists are more common than tuples, mostly because they are mutable. But there are a few
    cases where you might prefer tuples:
        1. In some contexts, like a return statement, it is syntactically simpler to create a tuple
        than a list.
        2. If you want to use a sequence as a dictionary key, you have to use an immutable type
        like a tuple or string.
        3. If you are passing a sequence as an argument to a function, using tuples reduces the
        potential for unexpected behavior due to aliasing.

    Because tuples are immutable, they don’t provide methods like sort and reverse, which
    modify existing lists. But Python provides the built-in function sorted, which takes any
    sequence and returns a new list with the same elements in sorted order, and reversed,
    which takes a sequence and returns an iterator that traverses the list in reverse order.
"""
t = tuple()
print(t)
print(type(t))
t = tuple("ashok")
print(t)
print(t[0])
print(t[0])
addr = 'monty@python.org'
uname,dname=addr.split("@")  ##multiple assignment can be done in a single statement
print(uname)
print(dname)
quot, rem=divmod(7, 3)   ##since this return values, can be assignd to multiple variable at the same itme

def min_max(t):
    return min(t),max(t)
#t=tuple("233498677534")
t="233498677534"
print(min_max(t))

def sum_all(*t):
    return sum(t)
##print(sum(1,2,3))  #TypeError: sum() takes at most 2 arguments (3 given)
print(sum_all(1,2,3,4,5,6,7))
print(sum_all(1,2,3))

###########   structshape  Lists, dictionaries and tuples are examples of data structures
#in this chapter we are starting to see compound data structures, like lists of tuples, or dictionaries that contain
#tuples as keys and lists as values.
t = [1, 2, 3]
print(structshape(t)) #'list of 3 int'
t2 = [[1,2], [3,4], [5,6]]
print(structshape(t2)) #'list of 3 list of 2 int'
t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
print(structshape(t3)) #list of (3 int, float, 2 str, 2 list of int, int)
s = 'abc'
lt = list(zip(t, s))
print(structshape(lt)) #list of 3 tuple of (int, str)
d=dict(lt)
print(structshape(d)) #dict of 3 int->str
