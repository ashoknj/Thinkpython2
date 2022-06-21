"""
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).

"""
fin=open("chapter9\words.txt")
for f in fin:
    if len(f.strip())>=20:
        print(f)



