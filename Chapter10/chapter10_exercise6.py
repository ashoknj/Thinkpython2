"""
Two words are anagrams if you can rearrange the letters from one to spell the other. Write
a function called is_anagram that takes two strings and returns True if they are anagrams
"""

def is_anagram(str1,str2):
        return sorted(str1)==sorted(str2)

print(is_anagram("hello","hlloe"))

