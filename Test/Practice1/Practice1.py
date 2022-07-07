
"""
Question 1
"""
def dictTest(d, s):
    isKey = []
    for char in s:
        if char not in d:
            continue
        elif char not in isKey:
            isKey.append(char)
    return len(isKey)

childDictionary = {'a':'apple','b':'bubble'}
print(dictTest(childDictionary, 'sappy'))

"""
Question 2
"""
def isPrefix(a, b):
    prefix = ''
    index = 0
    for letter in b:
        if index >= len(a):
            return a
        elif a[index] != b[index]:
            return prefix
        else:
            prefix += b
            index += 1
    return prefix
word0 = 'asp'
word1 = 'asparagus'
print(isPrefix(word0, word1))
"""
Question 3

"""
def isSub(aString):
    words = aString.split()
    left = 0
    right = -1
    for word in words:
        if words[left] not in words[right]:
            return word
        left += 1
        right -= 1
    return ""
s = 'horse sense is nonsense horseradish'
print(isSub(s))

"""
Question 4
"""
charSequence = 'toff'
prev = ""
for char in charSequence:
    if prev == "":
        prev = char
        out = ""
        continue
    elif char == prev:
        prev = char
        out = char
        break
    else:
        prev = char
        out = charSequence
print(out)

digits = {1:'one', 0:'z', 2:'two', 'zero':0}
#print(digits[0][1]) #index out of range
"""
Question 6
"""
fred = "Power concedes nothing without a demand"
def property(t, i):
    wordList = t.split()
    d = {}
    for word in wordList:
        length = len(word)
        if length%i == 0:
            continue
        if length not in d:
            d[length] = 1
        else:
            d[length] += 1
    return len(d)
print(property(fred, 2))
"""
Question 7

fats = ['you', 'were', 'my', 'thrill', 'on', 'Blueberry', 'Hill']
loopCount = 0
idx = 1
while len(fats[idx]) < len(fats):
    idx = len(fats[idx])
    loopCount += 1
print(loopCount) # infinite loop

"""


"""
Question 8
"""
bools = [True or False, True, False, True and False]
output = 0
for i in range(len(bools)):
    if bools[i]:
        output += 1
    else:
        output *= 2
print(output)

"""
Question 9
"""
subjects = {'languages':['Python','Java'], 'math':['algebra', 'calculus']}
#print(subjects[0][1]) #key error
print(subjects["languages"])

"""
Question 10
"""

def lookInto(inFile, outFile, searchString):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')
    for line in inF:
        instances = line.count(searchString)
        outF.write(str(instances))
    inF.close()
    outF.close()

lookInto('Test/lewis.txt', 'Test/out.txt', 'the')
