"""
lstrip([chars])    - Same concept applies to rstrip([chars])
Return a copy of the string with leading characters removed. 
The chars argument is a string specifying the set of characters to be removed. If omitted or None, 
the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather
, all combinations of its values are stripped:
"""
print('   spacious   '.lstrip()) #spacious   '
print('www.example.com'.lstrip('cmowz.'))  #'example.com'

###    str.removeprefix() for a method that will remove a single prefix string rather than all of a set of characters. For example
print('Arthur: three!'.lstrip('Arthur: ')) #'ee!'   it removes of occurances of the letters found in Arthur:
print('Arthur: three!'.removeprefix('Arthur: ')) #'three!'

"""
strip([chars])
Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying 
the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. 
The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

"""
print('   spacious   '.strip()) #spacious'
print('www.example.com'.strip('cmowz.'))  #'example'


"""
split(sep=None, maxsplit=- 1)
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, 
at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

"""

print('1,2,3'.split(',')) #['1', '2', '3']
print('1,2,3'.split(',', maxsplit=1)) #['1', '2,3']
print('1,2,,3,'.split(',')) #['1', '2', '', '3', '']