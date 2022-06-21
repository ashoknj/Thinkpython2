"""
Write a function named avoids that takes a word and a string of forbidden letters, and that
returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then
print the number of words that don’t contain any of them. Can you find a combination of
five forbidden letters that excludes the smallest number of words?
"""


def avoid(word,forbid):
    orglen=len(word)
    newlen=len(word.strip(forbid))
    if orglen==newlen:
        return True
    else:
        return False

def check_avoid():
    forbid=input("Enter the forbidden letters")
    fin=open("chapter9\words.txt")
    #fin=open("chapter9\\abc.txt")
    #print(forbid)
    for f in fin:
        found_status=False
        for t in forbid:
            if f.find(t)>0:
                found_status=True
                break
        if found_status==False:
            print(f)


#print(avoid("ashok","A"))
check_avoid()
#print("ashok".strip("h"))
#print("ashok".find("sk"))
