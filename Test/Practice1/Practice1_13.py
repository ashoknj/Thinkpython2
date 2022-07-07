"""
Write a function named lineStats. The function lineStats takes three parameters:
1. inFile, a string that is the name of an input file
2. outFile, a string that is the name of an output file
3. threshold, an int that is the length above which a word is considered significant
The function lineStats should read and analyze each line of the input file and write two statistics,
separated by a space, about the line to a corresponding line of the output file.
The two statistics for each line are:
1. the number of words
2. the number of distinct significant words (that is, words longer than threshold)
Hint: if a word occurs more than once on a line it counts as a single word.
Upper and lower case characters are considered the same ('Word' and 'word' are the same word).
The input file contains only upper and lower case letters and white space.
For example, if the file fish.txt contains the following lines:
Yes some are red and some are blue
Some are old and some are new
Then the function call:
lineStats('fish.txt', 'fishOut.txt', 3)
should produce an output file fishOut.txt with the following content:
8 2
7 1

"""
def lineStats(inFile,outFile,threshold):
    inputfile=open(inFile,"r")
    outputfile=open(outFile,"w")
    
    for line in inputfile:
        words=line.lower().split()
        uniquewords=[]
        threshold_word=0
        for w in words:
            if len(w)>threshold and w not in uniquewords:
                threshold_word+=1
                if w not in uniquewords:
                    uniquewords.append(w)
        outputfile.write(str(len(words))+" "+str(threshold_word)+"\n")
    inputfile.close()
    outputfile.close()

lineStats("Test/fish.txt","Test/fish_out.txt",3)