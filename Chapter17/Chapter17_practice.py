"""
            Classes and Methods
    Python is an object-oriented programming language,which has these defining characteristics:
    ~ Programs include class and method definitions.
    ~ Most of the computation is expressed in terms of operations on objects.
    ~ Objects often represent things in the real world, and methods often correspond to the
      ways things in the real world interact.
## method
    a method is a function that is associated
    with a particular class. We have seen methods for strings, lists, dictionaries and tuples. In
    this chapter, we will define methods for programmer-defined types.

    Methods are semantically the same as functions, but there are two syntactic differences:
    # Methods are defined inside a class definition in order to make the relationship between
      the class and the method explicit.
    # The syntax for invoking a method is different from the syntax for calling a function.

IMP Twos way to invole a function
    # one way to call the class.  classname.methodname(object) [less common way]
    # second one object.method name

    EX:
    class Time:
        def print_time(time):
            print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
        start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 00
    Time.print_time(start)  # one way to call the class.  classname.methodname(object) [less common way]
                            # “Hey print_time! Here’s an object for you to print.”
    start.print_time()  # Inside the method, the subject is assigned to the first parameter, so in this case start is assigned to time.
                        #start.print_time() says “Hey start! Please print yourself.”
IMP  Parameter self
    By convention, the first parameter of a method is called self, so it would be more
    common to write print_time like this:
    class Time:
        def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    
    ## for multiple parameter, the first one would be the self
        def increment(self, seconds):
            seconds += self.time_to_int()
            return int_to_time(seconds)
    invoke the method
        >>> start.print_time()
        09:45:00
        >>> end = start.increment(1337)
        >>> end.print_time()
        10:07:17
    The subject, start, gets assigned to the first parameter, self. The argument, 1337, gets
    assigned to the second parameter, seconds.
    
    ## positional argument and keyword argument
    a positional argument is an argument that doesn’t have a parameter name;
    that is, it is not a keyword argument. In this function call:
        sketch(parrot, cage, dead=True)
            parrot and cage are positional, and dead is a keyword argument.

    ## multiple object as arguement, 1st one will be a self
    # inside class Time:
        def is_after(self, other):
            return self.time_to_int() > other.time_to_int()
    To use this method, you have to invoke it on one object and pass the other as an argument:
        >>> end.is_after(start)
        True
    One nice thing about this syntax is that it almost reads like English: “end is after start?”

#### The __init__ Method
    The init method (short for “initialization”) is a special method that gets invoked when an
    object is instantiated. It's like a constructor
    # inside class Time:
        def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.minute = minute
            self.second = second
    It is common for the parameters of __init__ to have the same names as the attributes. The
    statement
        self.hour = hour
    stores the value of the parameter hour as an attribute of self.
    The parameters are optional, so if you call Time with no arguments, you get the default
    values: And if you provide three arguments, they override all three default values.
    >>> time = Time()
    >>> time.print_time()
    00:00:00
#### The __str__ Method

    __str__ is a special method, like __init__, that is supposed to return a string
    representation of an object.
    For example, here is a str method for Time objects:
    # inside class Time:
        def __str__(self):
            return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    When you print an object, Python invokes the str method:
        >>> time = Time(9, 45)
        >>> print(time)
        09:45:00
    When I write a new class, I almost always start by writing __init__, which makes it
    easier to instantiate objects, and __str__, which is useful for debugging.

#### Operator Overloading
    For example, if you define a method named __add__ for the
    Time class, you can use the + operator on Time objects
    # inside class Time:
        def __add__(self, other):
            seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    And here is how you could use it:
        >>> start = Time(9, 45)
        >>> duration = Time(1, 35)
        >>> print(start + duration)
        11:20:00
    When you apply the + operator to Time objects, Python invokes __add__. When you print
    the result,
IMP  Many such method can be found here http://docs.python.org/3/reference/datamodel.html#specialnames.

#### Type-Based Dispatch
    the prcess of checking the type of the argument whether it's an object or integrater or other data type and invoving the 
    methods is called Type-based dispatch

    The following is a version of __add__ that checks the type of
    other and invokes either add_time or increment:
    # inside class Time:
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
    return int_to_time(seconds)
    
    def increment(self, seconds):
        seconds += self.time_to_int()
    return int_to_time(seconds)

    The built-in function isinstance takes a value and a class object, and returns True if the
    value is an instance of the class.

    Here are examples that use the + operator with different types:
        >>> start = Time(9, 45)
        >>> duration = Time(1, 35)
        >>> print(start + duration)
        11:20:00
        >>> print(start + 1337)
        10:07:17
    ***  >>> print(1337 + start)
        TypeError: unsupported operand type(s) for +: 'int' and 'instance'
     To fix that the use special method __radd__, which stands for “right-side add”.
     # inside class Time:
        def __radd__(self, other):
            return self.__add__(other)
    And here’s how it’s used:
    >>> print(1337 + start)
    10:07:17

####      Polymorphism
    Functions that work with several types are called polymorphic.
    Type-based dispatch is useful when it is necessary, but (fortunately) it is not always
    necessary. Often you can avoid it by writing functions that work correctly for arguments
    with different types.
    Many of the functions we wrote for strings also work for other sequence types. For
    example, in “Dictionary as a Collection of Counters” we used histogram to count the
    number of times each letter appears in a word:
        def histogram(s):
            d = dict()
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] = d[c]+1
            return d
    This function also works for lists, tuples, and even dictionaries, as long as the elements of
    s are hashable, so they can be used as keys in d:
    
    >>> t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
    >>> histogram(t)
    {'bacon': 1, 'egg': 1, 'spam': 4}

For example, the built-in function sum, which adds the elements of a
sequence, works as long as the elements of the sequence support addition.
Since Time objects provide an add method, they work with sum:
    >>> t1 = Time(7, 43)
    >>> t2 = Time(7, 41)
    >>> t3 = Time(7, 37)
    >>> total = sum([t1, t2, t3])
    >>> print(total)
    23:01:00
####  Interface and Implementation
    https://realpython.com/python-interface/
    
    At a high level, an interface acts as a blueprint for designing classes. Like classes, interfaces define methods. Unlike classes, these methods are abstract. An abstract method is one that the interface simply defines. It doesn’t implement the methods. This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods.
    Python’s approach to interface design is somewhat different when compared to languages like Java, Go, and C++. These languages all have an interface keyword, while Python does not. Python further deviates from other languages in one other aspect. It doesn’t require the class that’s implementing the interface to define all of the interface’s abstract methods.

#### Debugging  hasattr  function, vars function
    If you are not sure whether an object has a particular attribute, you can use the built-in
    function hasattr

    Another way to access attributes is the built-in function vars, which takes an object and
    returns a dictionary that maps from attribute names (as strings) to their values:
    >>> p = Point(3, 4)
    >>> vars(p)
    {'y': 4, 'x': 3}
    For purposes of debugging, you might find it useful to keep this function handy:
        def print_attributes(obj):
            for attr in vars(obj):
                print(attr, getattr(obj, attr))
    print_attributes traverses the dictionary and prints each attribute name and its
    corresponding value.

"""
class Time:
    #def print_time(time):
    #    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    def __init__(self, hour=0, minute=0, second=0):
            self.hour = hour
            self.minute = minute
            self.second = second
    def __str__(self):
            return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 00
#Time.print_time(start)  # one way to call the class.  classname.methodname(object) [less common way]
                        # “Hey print_time! Here’s an object for you to print.”
#start.print_time()  # Inside the method, the subject is assigned to the first parameter, so in this case start is assigned to time.
                    #start.print_time() says “Hey start! Please print yourself.”

t1=Time()
t1.print_time()
t2=Time(9)
t2.print_time()
t3=Time(9,4,55)
print(t3)  ## here when printing object __str__ method is invoked.

