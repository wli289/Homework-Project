def divide_01(n):
    """ divide [0,1] into n pieces, using 1 line """
    return [numerator/float(n) for numerator in range(n)]

print divide_01(10)
print [element for element in range(10) if element%2 == 0]
print range(0,10,2)

def reverse_lec1(list_2rev):
    """ Reverses the order of a list IN PLACE
        NOTE: UNTESTED!! (there IS a problem in the code)
    """
    count = 0
    while count < len(list_2rev):
        new_element = list_2rev.pop(0)
        list_2rev.insert(len(list_2rev)-count,new_element)
        count += 1
        #print list_2rev

def reverse(some_list):
    """ reverse the order of elements IN PLACE """
    count = len(some_list)-2
    while count >= 0:
        element = some_list[count]
        some_list.append(element)
        some_list.pop(count)
        count -= 1

a = [1,2,3]
b = a
b.append(6)
#print "a:", a
#print "b:", b

# modify the list "in place"
import random
random.shuffle(a)
#print "a:", a

# test our reverse function
#reverse(a)
#print "a:", a
x = range(10)
reverse(x)
print "x:", x
reverse_lec1(x)
print "x:", x
"""
# deep copy of x
x_copy = []
for element in x:
    x_copy.append(element)  # calculation
random.shuffle(x_copy)
print "x:", x
print "x copy:", x_copy

# list comprehension deep copy
x_copy2 = [element for element in x]
x_copy2.pop(0)
print "x:", x
print "x copy2:", x_copy2
"""
