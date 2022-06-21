"""
In 1939 Ernest Vincent Wright published a 50,000-word novel called Gadsby that does not
contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.
In fact, it is difficult to construct a solitary thought without using that most common
symbol. It is slow going at first, but with caution and hours of training you can gradually
gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it.
Modify your program from the previous section to print only the words that have no “e”
and compute the percentage of the words in the list that have no “e”.
"""

def has_no_e(word):
    if word.find("e") !=-1:   ## return -1 when no matching found
        return True
    else:
        return False

def no_e_analysis():
    fin=open("chapter9\words.txt")
    total_words=0
    words_with_no_e=0

    for f in fin:
        total_words=total_words+1
        if has_no_e(f)==True:
            words_with_no_e=words_with_no_e+1
    return (words_with_no_e/total_words)*100

#print(has_no_e("aeshok"))
print("Percentage of words with no e: %s %%" % round(no_e_analysis()))
