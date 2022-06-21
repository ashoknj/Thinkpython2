"""
Write a function named uses_only that takes a word and a string of letters, and that
returns True if the word contains only letters in the list. Can you make a sentence using
only the letters acefhlo? Other than “Hoe alfalfa?”
"""
def only_inside(word,forbid):
    for w in word:
        found_status=True
        if forbid.find(w)==-1:
            found_status=False
            break
    if found_status==True:
        print(word)
    else:
        print("No words with all those letters")    

only_inside("ratw","raqwerddtq")