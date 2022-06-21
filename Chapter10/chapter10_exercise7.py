"""
Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
"""
def has_duplicates(str1):
    str2=str1[:]
    str2.sort()
    i=0
    d=False
    while i<len(str2)-1:
        if str2[i]==str2[i+1]:
            d=True
            break
        i=i+1
    return d
def has_duplicate_for(s):
        t = list(s)
        t.sort()
        for i in range(len(t)-1):
            if t[i] == t[i+1]:
                return True
        return False

print(has_duplicates(['c','a','x','m']))
print(has_duplicate_for(['c','a','x','m']))