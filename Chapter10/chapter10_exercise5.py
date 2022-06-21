"""
Write a function called is_sorted that takes a list as a parameter and returns True if the
list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""

def is_sorted(t):
   t1=[]
   for x in t:
        t1.append(x)
   t.sort()
   if t1==t:
        return True
   else:
        return False

def is_sorted_short(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    """
    return t == sorted(t)

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
print(is_sorted_short([1, 2, 2]))
print(is_sorted_short(['b', 'a']))

