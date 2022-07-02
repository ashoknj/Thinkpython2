import os
import pickle
import wc
"""
                    FILES
persistent storage: they run for a long time (or all the time); they keep at least
some of their data in permanent storage (a hard drive, for example);              

pickle - store the state of the program in a database

#### Reading and Writing
    To write a file, you have to open it with mode 'w' as a second parameter:
    >>> fout = open('output.txt', 'w')  ## returns file object that provides methods for working with the file

If the file already exists, opening it in write mode clears out the old data and starts fresh,
so be careful! If the file doesn’t exist, a new one is created.

    >>> line1 = "This here's the wattle,\n"
    >>> fout.write(line1)  ## you can keep calling write multiple times The file object keeps track of where it is
    >>> fout.close() ##If you don’t close the file, it gets closed for you when the program ends.

### Format Operator
    The argument of write has to be a string, so if we want to put other values in a file, we
    have to convert them to strings. The easiest way to do that is with str:
        >>> x = 52
        >>> fout.write(str(x))

format string %d is for integer and %s for string,%g floating point number
    >>> 'I have spotted %d camels.' % camels
    'I have spotted 42 camels.
    >>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')    ## multiple values , should be in a Tuple
    'In 3 years I have spotted 0.1 camels.''

#### Filenames and Paths

    The os module provides functions for working with files and directories (“os” stands for
    “operating system”). os.getcwd returns the name of the current directory:
>>> import os
>>> cwd = os.getcwd()
>>> cwd
'/home/dinsdale'

    check whether folder or file exists
    >>> os.path.isdir('/home/dinsdale')
    >>> os.path.isfile("Chapter9/words.txt")
    to get the folders/files
    >>> os.listdir(cwd)

#### Catching Exceptions
    try:
    fin = open('bad_file')
    except:            #end the program gracefully.
    print('Something went wrong.')  

#### Databases
    Python provides a database API that is very useful when needed to work with different type of databases. The data are stored within a DBM (database manager) 
    persistent dictionaries that work like normal Python dictionaries except that the data is written to and read from disk.

    >>> import dbm
    >>> db = dbm.open('captions', 'c')  #The mode 'c' means that the database should be created if it doesn’t already exist
    
    When you create a new item, dbm updates the database file:
    >>> db['cleese.png'] = 'Photo of John Cleese.'

    When you access one of the items, dbm reads the file:
    >>> db['cleese.png']  #The result is a bytes object, which is why it begins with b.
    b'Photo of John Cleese.'

IMP Some dictionary methods, like keys and items, don’t work with database objects. But
    iteration with a for loop works:
    
        for key in db:
            print(key, db[key])
    
    As with other files, you should close the database when you are done:
    >>> db.close()
####  PICKLE
    Pickling" is process which enables storage and preservation
    
    Pickle in Python is primarily used in serializing and deserializing a Python object structure. In other words, 
    it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state
    across sessions, or transport data over the network.

    The pickle module can help. It translates almost any type of object into a string suitable
    for storage in a database, and then translates strings back into objects.

    pickle.dumps takes an object as a parameter and returns a string representation (dumps is
    short for “dump string”):

    >>> import pickle
    >>> t = [1, 2, 3]
    >>> pickle.dumps(t)
    b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

    >>> t1 = [1, 2, 3]
    >>> s = pickle.dumps(t1)
    >>> t2 = pickle.loads(s)
    >>> t2
    [1, 2, 3]

    Although the new object has the same value as the old, it is not (in general) the same
    object:
    >>> t1 == t2
    True
    >>> t1 is t2
    False

####  Pipes
    Any program that you can launch from the shell can also be launched from Python using a
    pipe object, which represents a running program.

    >>> cmd = 'dir'   ## to show the list of files 
    >>> fp = os.popen(cmd)

    You can read the output using read

    >>> res = fp.read()
    
    When you are done, you close the pipe like a file:
    >>> stat = fp.close()
    >>> print(stat)
    None

    The return value is the final status of the dir process; None means that it ended normally
    (with no errors).
### unix checksum md5sum module

    >>> filename = 'book.tex'
    >>> cmd = 'md5sum ' + filename
    >>> fp = os.popen(cmd)
    >>> res = fp.read()
    >>> stat = fp.close()
    >>> print(res)
    1e0033f0ed0656636de0d75144ba32e0 book.tex
    >>> print(stat)
    None

### Writing Modules
Any file that contains Python code can be imported as a module. For example, suppose
you have a file named wc.py with the following code:
    def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count
    print(linecount('wc.py'))
    
    If you run this program, it reads itself and prints the number of lines in the file, which is 7.
    You can also import it like this:
    >>> import wc
    7
    The module object provides linecount:
    >>> wc.linecount('wc.py')
    7

IMP
    Programs that will be imported as modules often use the following idiom:
    if __name__ == '__main__':
    print(linecount('wc.py'))
    
    __name__ is a built-in variable that is set when the program starts. If the program is
    running as a script, __name__ has the value '__main__'; in that case, the test code runs.
    Otherwise, if the module is being imported, the test code is skipped.
    As an exercise, type this example into a file named wc.py and run it as a script. Then run
    the Python interpreter and import wc. What is the value of __name__ when the module is
    being imported?
    Warning: If you import a module that has already been imported, Python does nothing. It
    does not re-read the file, even if it has changed.
    If you want to reload a module, you can use the built-in function reload, but it can be
    tricky, so the safest thing to do is restart the interpreter and then import the module again.

###   debugging  - built-in function repr can help

    When you are reading and writing files, you might run into problems with whitespace.
    These errors can be hard to debug because spaces, tabs and newlines are normally
    invisible:
        >>> s = '1 2\t 3\n 4'
        >>> print(s)
        1 2 3
        4
    The built-in function repr can help. It takes any object as an argument and returns a string
    representation of the object. For strings, it represents whitespace characters with backslash
    sequences:
    >>> print(repr(s))
    '1 2\t 3\n 4'


"""
cwd = os.getcwd()
print(cwd)
print(os.path.isdir("Chapter1"))
print(os.path.isfile("Chapter9/words.txt"))
print(os.path.abspath("words.txt"))   ## return the absolute path whether file exists or not
print(os.listdir(cwd)) #returns a list of the files (and other directories) in the given directory:

#To demonstrate these functions, the following example “walks” through a directory, prints
#the names of all the files, and calls itself recursively on all the directories:

def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name) #os.path.join takes a directory and a filename and joins them into a complete path
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
#walk("c:\karan")

t=[1,2,3]
s=pickle.dumps(t)
print(s)
t2=pickle.loads(s)
print(t2)


cmd = 'dir'
fp = os.popen(cmd)
res = fp.read()

#print(res)
print(__name__)