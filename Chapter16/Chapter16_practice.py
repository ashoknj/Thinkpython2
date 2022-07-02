"""
    Classes and Functions

#### Pure Functions

Here is a simple prototype of add_time:
    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
    return sum

    The function creates a new Time object, initializes its attributes, and returns a reference to
    the new object. This is called a pure function because it does not modify any of the
    objects passed to it as arguments and it has no effect, like displaying a value or getting
    user input, other than returning a value.

### Modifier
    Sometimes it is useful for a function to modify the objects it gets as parameters. In that
    case, the changes are visible to the caller. Functions that work this way are called
    modifiers.

increment, which adds a given number of seconds to a Time object, can be written
naturally as a modifier. Here is a rough draft:
    def increment(time, seconds):
        time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -=

IMP** In general, I recommend that you write pure functions whenever it is reasonable and resort
    to modifiers only if there is a compelling advantage. This approach might be called a
    functional programming style.

#### Debugging  - assert statement
    assert statement, which checks a given invariant and raises an     exception if it fails:
    def add_time(t1, t2):
        assert valid_time(t1) and valid_time(t2)
        seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

    assert statements are useful because they distinguish code that deals with normal
    conditions from code that checks for errors.

    EX: 

    x = "hello"

    #if condition returns True, then nothing happens:
    assert x == "hello"

    #if condition returns False, AssertionError is raised:
    assert x == "goodbye"



"""
class Time:
     """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):

    """Prints a string representation of the time.
    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum
start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
print_time(done)

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"