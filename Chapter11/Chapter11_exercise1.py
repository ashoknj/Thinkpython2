"""
Write a function that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
If you did Exercise 10-10, you can compare the speed of this implementation with the list
in operator and the bisection search.

"""
import time
def create_dict(s):
    d=dict()
    fin=open("chapter9\words.txt")
    for f in fin:
        if f not in d:
            d[f.strip()]=1
    if s in d:
        return True
    else:
        return False
    

starttime=time.time()
#print(create_dict("acidities"))
print(create_dict("Ashok"))
endtime=time.time()
print("Total time taken %d:",endtime-starttime)

    
