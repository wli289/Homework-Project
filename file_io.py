# read in a file

f = open("./to_read.txt", "r")
print type(f)
lines = f.readlines()
for line in lines:
    print line,       # don't print a new line
    print line[:-1]   # chop off the \n character
f.close()

f = open("./mystery.txt", 'r')
print f.readline()
print f.readline()

lines = f.readlines()
print lines[0]

f.close()

# read a file in a for loop
poem1 = []
poem2 = []
is_poem1 = True
#new_f = open("./mystery.txt",'r')
with open("./mystery.txt",'r') as new_f:
    for x in new_f:
        if is_poem1:
            poem1.append(x[:-1]) # remove newline character
        else:
            poem2.append(x[:-1])
        is_poem1 = not is_poem1
#new_f.close()   # this is already done!
#print poem1

# write poem2 to a file
outfile = raw_input("Where should we write to? ")
with open(outfile, 'w') as out:
    for line in poem2:
        out.write(line + "\n")

import os
filename = raw_input("What file should we open? ")
if os.path.exists(filename):
    with open(filename, 'r') as user_file:
        print user_file.readline()

test_file = raw_input("What file should we test? ")
with open(test_file, 'a'):
    print "hi"
