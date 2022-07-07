"""
Assume that the code for the class State (Question 11A) has been saved in a file named state.py. Write
code that performs the following tasks (each task takes one line):
1. import the module that defines the class State
2. create a state named New Jersey
3. add universities NJIT and Princeton to New Jersey
4. check whether New Jersey is home of MIT and print the result

"""
import Practice1_11A as s

nj=s.state("New Jersey")
nj.add_university("NJIT")
nj.add_university("Princeton")
print(nj.is_home_of("MIT"))
