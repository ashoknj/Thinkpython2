"""
Write a function called nested_sum that takes a list of lists of integers and adds up the
elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""

def nested_sum(t):
    total=0
    for x in t:
        total=total+sum(x)
    return total

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
