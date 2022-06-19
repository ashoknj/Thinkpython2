""""palindrome
 A palindrome is a word that is spelled the same backward and forward, like “noon” and
“redivider”. Recursively, a word is a palindrome if the first and last letters are the same
and the middle is a palindrome.
"""
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    result=False
    f=first(word)    
    l=last(word)
    print(f)
    print(l)
    if f==l:
        if len(middle(word))==1 or middle(word)=='':
            print("inside length comp")
            result=True
        else:
            r=middle(word)
            print(r)
            return is_palindrome(r)   # the inside recursive should have return statement otheriwise it will retunr Nome
    else:
        result=False
    return result
 
#print(first("a"))
#print(last("a"))
#if middle("aa")=='':
#    print("No middle")
#else:
#    print(middle("aa"))
print(is_palindrome("ak"))