"""
Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
that is, a new list where the ith element is the sum of the first i+1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

"""
def cumsum(t):
    s=[]
    total=0
    for x in t:
        total=total+x
        s.append(total)
    return s
t = [1, 2, 3]
print(cumsum(t))
