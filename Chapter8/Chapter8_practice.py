#########       string manipulation
fruit="banana"
#print(fruit[0])  #index starts with 0
#print(fruit[-1])  #retrive last letter
#print(fruit[-2])  #2nd from the last letter
#print(len(fruit))  #shows length

# traves through a loop
for letter in fruit:
    print(letter)
"""
In Robert McCloskey’s book
Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
Ouack, Pack, and Quack. This loop outputs these names in order:

"""
text="JKLMNOPQ"
prefix="ack"
for letter in text:
    if letter=="O" or letter=="Q":
        letter=letter+"u"
    print(letter+prefix)

""" String Slices
The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth”
character, including the first but excluding the last
If you omit the first index (before the colon), the slice starts at the beginning of the string.
If you omit the second index, the slice goes to the end of the string:
"""
s="Awesome Python"
print(s[0:7])  # print Awesome
print(s[8:14])  # print Awesome
print(s[8:])  # from 8th position till end of the string 
print(s[:7])  # from beginning till 6th position exclusing 7th position
print(s[3:3]) #If the first index is greater than or equal to the second the result is an empty string,
print(s[:]) #returns the whole string

####   Strings Are Immutable
#fruit[0]="a" Gives error object does not support item assignment
## String Method  upper, find

print(fruit.upper())
print(fruit.find("na",1,4)) #returns the index, 2nd and 3rd are option parameter of start and end index [if excludes the last index]
print(fruit.find("k")) #returns -1 if no match found 

#####    in operator
print("a" in fruit)  #returns True
print("na" in fruit)  #returns True
#Ex: PRINT all the letter from word 1 which are found in word2
def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

#in_both("ashok","suman")
#in_both("Kashvi","Karan")
in_both("karan","suman")

#####    string comparision   == > < [relational operations are useful for putting words in alphabetical order]
word="bananax"
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')

# 3rd argument is optionl , it is the step size, 2 means every other characcter, - means starts towrds a end
print(fruit[::-1])  #This prints the reverse of the string



