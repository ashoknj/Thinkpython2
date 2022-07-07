"""
Write a function named wordLineCount with the following input and output:
Input: a string parameter, inFile, that is the name of a file
Output: return a dictionary in which each unique word in inFile is a key and the corresponding 
value is the number of lines on which that word occurs
The file inFile contains only lower case letters and white space.
For example, if the file ben.txt contains these lines:
tell me and i forget
teach me and i remember
involve me and i learn
then the following would be correct output:
>>> print(wordLineCount('ben.txt'))
{'tell': 1, 'me': 3, 'and': 3, 'i': 3, 'forget': 1, 'teach': 1, 'remember': 1, 'involve':
1, 'learn': 1}

"""
def wordLineCount(inFile):
    finallist={}
    for line in open(inFile):
        words=line.split()
        print(type(words))
        for w in words:
            if w not in finallist:
                finallist[w]=1
            else:
                finallist[w]+=1
    return finallist
  
print(wordLineCount("Test/ben.txt"))
