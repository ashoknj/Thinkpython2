from __future__ import print_function, division

import shelve
import sys

from Chapter12_exercise2 import all_anagrams, signature


"""
If you download my solution to Exercise 12-2 from
http://thinkpython2.com/code/anagram_sets.py, you’ll see that it creates a dictionary that
maps from a sorted string of letters to the list of words that can be spelled with those
letters. For example, 'opst' maps to the list ['opts', 'post', 'pots', 'spot',
'stop', 'tops'].
Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”; read_anagrams should
look up a word and return a list of its anagrams.

"""
"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""


def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.
    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.
    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('Chapter9/words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)