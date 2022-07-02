"""
##########################  Dictionaries

definition:
    A dictionary is like a list, but more general. In a list, the indices have to be integers; in a
    dictionary they can be (almost) any type.
    A dictionary contains a collection of indices, which are called keys, and a collection of
    values. Each key is associated with a single value. The association of a key and a value is
    called a key-value pair or sometimes an item.

syntax:
    The function dict creates a new dictionary with no items. Because dict is the name of a
    built-in function, you should avoid using it as a variable name.
    >>> eng2sp = dict()
    >>> eng2sp
    {}

EX:
    The squiggly brackets, {}, represent an empty dictionary. To add items to the dictionary,
    you can use square brackets:
    >>> eng2sp['one'] = 'uno'
    This line creates an item that maps from the key 'one' to the value 'uno'. If we print the
    dictionary again, we see a key-value pair with a colon between the key and value:
    >>> eng2sp
    {'one': 'uno'}

    This output format is also an input format. For example, you can create a new dictionary
    with three items:
    >>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    
    But if you print eng2sp, you might be surprised:
    >>> eng2sp
    {'one': 'uno', 'three': 'tres', 'two': 'dos'}
IMP: The order of the key-value pairs might not be the same. If you type the same example on
     your computer, you might get a different result. In general, the order of items in a
     dictionary is unpredictable.

######     function
len - the number of key-value pairs:
The in operator - it tells you whether something appears as a key 
    [
        The in operator uses different algorithms for lists and dictionaries. For lists, it searches the
        elements of the list in order, as in “Searching”. As the list gets longer, the search time gets
        longer in direct proportion.
        For dictionaries, Python uses an algorithm called a hashtable that has a remarkable
        property:   
        ]
values() - returns a collection of values. we can then use the in operator to search something in the value
in the dictionary

Dictionary value can be a list as well EX : {1: ['a', 'p', 't', 'o'], 2: ['r']}
Dictionary keys can not be a list as list is mutable where as keys are hashable



"""
a=dict()
print(a)
a["name"]="Ashok"
a["age"]="18"
print(a)
a={"name":"Muna","age":36}
print(a)
print(a["age"])
print(len(a))
print("age1" in  a)
vals=a.values()
print(36 in vals)
#### EX Dictionary as a Collection of Counters

def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:    
            d[c]+=1
    return d

h=histogram('brontosaurus')
#print(h)   

#### Looping and Dictionaries
for x in sorted(h):
    print(x,h[x])

#### Reverse Lookup   look up the key based on the value
def reverse_lookup(d,v):
    for k in d:
        if d[k]==v:
            return k
    raise LookupError("value does not appear in the dictionary")

h = histogram('parrot')
k = reverse_lookup(h, 2)
#k = reverse_lookup(h, 2)
print(k)

#### Dictionaries and Lists
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print(hist)  #{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
inverse = invert_dict(hist)
print(inverse) #{1: ['a', 'p', 't', 'o'], 2: ['r']}
"""
I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be hashable.
A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries
use these integers, called hash values, to store and look up key-value pairs.
This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,
or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.
That’s why keys have to be hashable, and why mutable types like lists aren’t. The simplest
way to get around this limitation is to use tuples, which we will see in the next chapter.
Since dictionaries are mutable, they can’t be used as keys, but they can be used as values.
"""


####   Memos (A previously computed value that is stored for later use is called a memo)
#If you run this version of fibonacci and compare it with the original, you will find that it is much faster
known = {0:0, 1:1}    
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(20))    

#### Global Variables
"""
In the previous example, known is created outside the function, so it belongs to the special
frame called __main__. Variables in __main__ are sometimes called global because they
can be accessed from any function. Unlike local variables, which disappear when their
function ends, global variables persist from one function call to the next.

It is common to use global variables for flags; that is, boolean variables that indicate
(“flag”) whether a condition is true

IMP : To reassign a global variable inside a function you have to declare the global variable
before you use it:


    count = 0
    def example3():
        count = count + 1 # WRONG
    
    If you run it you get:
        UnboundLocalError: local variable 'count' referenced before assignment Python assumes that count is local, and under that assumption you are reading it before
        writing it. The solution, again, is to declare count global:

    If a global variable refers to a mutable value, you can modify the value without declaring     the variable:
    known = {0:0, 1:1}
    def example4():
        known[2] = 1

## SET DEFAULT
Description
Python dictionary method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.

Syntax
Following is the syntax for setdefault() method −

dict.setdefault(key, default=None)
Parameters
key − This is the key to be searched.

default − This is the Value to be returned in case key is not found.

Return Value
This method returns the key value available in the dictionary and if given key is not available then it will return provided default value.


"""

been_called = False
def example2():
    global been_called
    been_called = True

print(been_called)
example2()
print(been_called)
