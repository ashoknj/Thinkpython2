"""
In a string, the values are characters; in a list,
they can be any type. The values in a list are called elements or sometimes items.
There are several ways to create a new list; the simplest is to enclose the elements in
square brackets ([ and ]):
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']

#############  a list within a list is called nested
['spam', 2.0, 5, [10, 20]]
empty list []
you can assign list values to variables
cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [42, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []

######  starings a mutable 
>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5]

#######   index starts with 0
List indices work the same way as string indices:
Any integer expression can be used as an index.
If you try to read or write an element that does not exist, you get an IndexError.
If an index has a negative value, it counts backward from the end of the list.
The in operator also works on lists:
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False

######  Traversing a list   mostly through fot loop
A for loop over an empty list never runs the body:
for x in []:
print('This never happens.')
###### List operation
+  concatinate list
* repeats a list given a number of times

####### List slicing [start:end]
the slice operator also works with list
If you omit the first index, the slice starts at the beginning. If you omit the second, the
slice goes to the end. So if you omit both, the slice is a copy of the whole list Ex [:]
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> t
['a', 'x', 'y', 'd', 'e', 'f']

###### list method   append, extend, sort
append adds a new element to the end of a list:
extend takes a list as an argument and appends all of the elements:
sort arranges the elements of the list from low to high:
Most list methods are void; they modify the list and return None.
sorted()  is the method which takes list as a argument and return true if the list is sorted

######  Map, filter, reduce
reduce
    >>> t = [1, 2, 3]
    >>> sum(t)
    6
Map
An operation like capitalize_all is sometimes called a map because it “maps” a
function (in this case the method capitalize) onto each of the elements in a sequence
    def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
Filter
An operation like only_upper is called a filter because it selects some of the elements and
filters out the others

    def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

Most common list operations can be expressed as a combination of map, filter and reduce.
######  deleting an element  pop, del, remove
pop(index)  remove the elements and allow you to store this value in a different variable
    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> t
    ['a', 'c']
    >>> x
    'b'
del
    If you don’t need the removed value, you can use the del operator:
    >>> t = ['a', 'b', 'c']
    >>> del t[1]
    >>> t
    ['a', 'c']
remove
    If you know the element you want to remove (but not the index), you can use remove:
    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> t
    ['a', 'c']
    The return value from remove is None.
        To remove more than one element, you can use del with a slice index:
    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> del t[1:5]
    >>> t
    ['a', 'f']
    As usual, the slice selects all the elements up to but not including the second index.

##### List and String  [list method, split method, join -> it is the inverse of split]
>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']

### onject and value
To check whether two variables refer to the same object, you can use the is operator:
    >>> a = 'banana'
    >>> b = 'banana'
    >>> a is b
    True

In this example, Python only created one string object, and both a and b refer to it. But
when you create two lists, you get two objects:
    >>> a = [1, 2, 3]
    >>> b = [1, 2, 3]
    >>> a is b
    False
    
    since list is mutable and string is immutable

Until now, we have been using “object” and “value” interchangeably, but it is more precise
to say that an object has a value. If you evaluate [1, 2, 3], you get a list object whose
value is a sequence of integers. If another list has the same elements, we say it has the
same value, but it is not the same object.

####  Aliasing

    If a refers to an object and you assign b = a, then both variables refer to the same object:
    >>> a = [1, 2, 3]
    >>> b = a
    >>> b is a
    True

The association of a variable with an object is called a reference. In this example, there
are two references to the same object.
An object with more than one reference has more than one name, so we say that the object
is aliased.
    If the aliased object is mutable, changes made with one alias affect the other:
    >>> b[0] = 42
    >>> a
    [42, 2, 3]
#######     List Arguments
    When you pass a list to a function, the function gets a reference to the list. If the function
    modifies the list, the caller sees the change. For example, delete_head removes the first
    element from a list:
    
        def delete_head(t):
            del t[0]
    
        Here’s how it is used:
        >>> letters = ['a', 'b', 'c']
        >>> delete_head(letters)
        >>> letters
        ['b', 'c']

    The parameter t and the variable letters are aliases for the same object

    An alternative is to write a function that creates and returns a new list. For example, tail
    returns all but the first element of a list:
        def tail(t):
            return t[1:]
    This function leaves the original list unmodified. Here’s how it is used:
    >>> letters = ['a', 'b', 'c']
    >>> rest = tail(letters)
    >>> rest
    ['b', 'c']

"""    
days=["Sunday","Monday","Tuesday"]
remain_days=["wed","thu","fri","sat"]
#for d in days:
    #print(d)

#print(days+remain_days)
#print(days*2) #repeat sun, mon, Tue two times 

#days.append("Wednesday")
#print(days)
days.extend(remain_days)
print(days)
days.sort()
print(days)

name="ashok"
t=list(name)  ## Convert string to list
print(t)

name="ashok kumar mehta"
sp=name.split() ## split into words
print(sp)
## now join the name with hypen as delimeter
delimeter="-"
s=delimeter.join(sp)
print(s)

def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
print(letters)  ## letters is unchanged

