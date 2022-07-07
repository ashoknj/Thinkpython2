"""
Write a definition line for a class named State and a one-line docstring that describes what a State is.
Write definitions for the following methods in the State class:
1. An initialization method. The initialization method should:
– take a string parameter, name, and assign it to the instance attribute name of the state being
created
– create an instance attribute named universities for the state being created and initialize
it to the empty list
2. A method named add_university. This method should take the name of a university as a string
parameter and add it to the list of universities for that state.
3. A method named is_home_of. This method should take the name of a university as a string
parameter. If the university is in the state’s list of universities it should return True, otherwise it
should return False.
"""


class state:
    def __init__(self,statename):
        self.name=statename
        self.universities=[]
    def add_university(self,name):
        self.universities.append(name)
    def is_home_of(self,name):
        if name in self.universities:
            return True
        else:
            return False

"""
nj=state("nj")
nj.add_university("princeton")
nj.add_university("rutgers")
print(nj.is_home_of("princeton"))
print(nj.is_home_of("abc"))

"""
