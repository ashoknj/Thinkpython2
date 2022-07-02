"""
If you did Exercise 10-7, you already have a function named has_duplicates that takes a
list as a parameter and returns True if there is any object that appears more than once in
the list.
Use a dictionary to write a faster, simpler version of has_duplicates
"""
def has_duplicates(str1):
    d=dict()
    for f in str1:
        if f in d:
            return True
        else:
            d[f]=1
    return False

def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.
    Faster version using a set.
    t: sequence
    """
    return len(set(t)) < len(t)
print(has_duplicates(['a','a','x','c']))
print(has_duplicates2(['a','a','x','c']))