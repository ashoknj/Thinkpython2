
## The floor division operator, //, divides two numbers and rounds down to an integer
minutes=175
hour=minutes//60
reminders=minutes-hour*60 # we can also use module operator
reminders=minutes%60
print(hour)
print(reminders)

## boolean operator  == , !=, >, <, >=, <=
print(5==5 )

## logical operator    and, or , not

## conditional operator   if else
x=11
if(x%2==0):
    print("Even number")
else:
    print("odd number")
## Chained conditional if elif
time=26
if(time>=0 and time<12):
    print("Good morning")
elif(time>=12 and time<17):
    print("Good afternoon")
elif(time>=17 and time<24):
    print("Good evening")
else:
    print("Invalid time")

###   nested conditional
x=4
y=3
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

#### recursion 
#A function that calls itself is recursive; the process of executing it is called recursion.

def countdonw(n):
    if(n==0):
        print("B:AST OFF!!!!!")
    else:
        print(n)
        countdonw(n-1)
#countdonw(5)

### range function range(start, stop, step)  it exclude the stop
#for i in range(4): #starts from 0 and goes till 3
#    print(i)
### Break and continue  Guess what could be the result value???
#The continue keyword is used to end the current iteration in a for loop and continues to the next iteration
#break - comes out of for and while loop
for i in range(6,20,1):
    if(i%2==0):
        continue
    if(i%5==0):
        print(i)
        print("Got the 1st number divisible by five")
        break
########    Infinite Recursion
"""If a recursion never reaches a base case, it goes on making recursive calls forever, and the
program never terminates. This is known as infinite recursion
In most programming environments, a program with infinite recursion does not really run
forever. Python reports an error message when the maximum recursion depth is reached:
"""
def inf_recur(n):
    inf_recur(n)
#inf_recur(10)

#########  ekyboard input
prompt="What is your name\n"
name=input(prompt)
print("Hello :"+name)
