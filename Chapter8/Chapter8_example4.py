## Returns True if the first character found as lowercase , due to return statement it doesn't loop through the entire string
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
## it's checking the character the 'c' always return True
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

## Returns True if the last character found as lowercase , asflag is overwritten

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
## Return True if any single lower character found
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

## Return True only if all characters are lower letter 

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#print(any_lowercase1("aSHOK"))
#print(any_lowercase1("ASHoK"))
#print(any_lowercase1("ASHOk"))

#print(any_lowercase2("aSHOK"))
#print(any_lowercase2("ASHoK"))
#print(any_lowercase2("ASHOk"))

#print(any_lowercase3("aSHOK"))
#print(any_lowercase3("ASHoK"))
#print(any_lowercase3("ASHOk"))

#print(any_lowercase4("aSHOK"))
#print(any_lowercase4("ASHoK"))
#print(any_lowercase4("ASHOk"))
#print(any_lowercase4("ASHOK"))

print(any_lowercase5("aSHOK"))
print(any_lowercase5("ASHoK"))
print(any_lowercase5("ASHOk"))
print(any_lowercase5("ASHOK"))
print(any_lowercase5("ashok"))