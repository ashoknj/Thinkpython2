"""
Write a function called is_abecedarian that returns True if the letters in a word appear in
alphabetical order (double letters are okay). How many abecedarian words are there?

"""

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian_recur(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recur(word[1:])

def is_abecedarian_while(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
           return False
        i = i+1
    return True

#print(is_abecedarian("ashok"))
#print(is_abecedarian("asz"))
#print(is_abecedarian_recur("ashok"))
#print(is_abecedarian_recur("asz"))
print(is_abecedarian_while("ashok"))
print(is_abecedarian_while("asz"))