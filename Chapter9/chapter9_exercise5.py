"""
Write a function named uses_all that takes a word and a string of required letters, and
that returns True if the word uses all the required letters at least once. How many words
are there that use all the vowels aeiou? How about aeiouy?
"""
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_short(word, required):   #reduction to a previously solved problem,
     return uses_only(required, word)

print(uses_only("ashok","ashokkhans"))
print(uses_all("ashok","ash"))
print(uses_all_short("ashok","ash"))
