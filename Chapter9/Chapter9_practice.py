##            Case Study: Word Play
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

"""
The %s specifier converts the object using str(), and %r converts it using repr().

For some objects such as integers, they yield the same result, but repr() is special in that 
(for types where this is possible) it conventionally returns a result that is valid Python syntax, 
which could be used to unambiguously recreate the object it represents.
"""

print("Files in %r: %s" % (cwd, files))
print("Files in %s: %s" % (cwd, files))

fin=open('chapter9/abc.txt')
print(fin.readline())


