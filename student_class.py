def fcn_name(parameters):
    """ does stuff """
    return 6

import random
class Student:
    def __init__(self,n):
        """ method to set up a Student object """
        self.name = n
        self.age = random.randint(18,25)
        self.year = 1
        self.num_credits = 0

    def take_class(self, credits):
        self.num_credits += credits
        if self.num_credits/30 > self.year-1:
            self.year += 1

s = Student("Bob")
print s.name     # equivalent of s['name']

a = Student("Hobbes")
print a.name     # equivalent of a['name']

s.take_class(4)
print a.num_credits
print s.num_credits
