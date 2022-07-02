def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count
if __name__ == '__main__':                ##The below code will not ne executed if we import this fie wc.py as a moodule im another file
    print(linecount('Chapter14/wc.py'))