"""

This question is based on a Puzzler that was broadcast on the radio program Car Talk
(http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-pi.
If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.

This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string
    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count  ## if the consecutive letter is not same, reset the count and start checking from previous letter again
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('chapter9/words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
