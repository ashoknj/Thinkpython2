from __future__ import print_function, division


from chapter10_exercise10 import in_bisect, make_word_list

"""
Two words are a “reverse pair” if each is the reverse of the other. Write a program that
finds all the reverse pairs in the word list.
Solution: http://thinkpython2.com/code/reverse_pair.py.

"""

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.
    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])
