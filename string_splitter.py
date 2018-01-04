""" Our goal: input - cat, output:
  *
 * *
* * *
c a t
"""

word = raw_input("Word:")

# step 3: print a box of stars above the word 
count3 = 0
while count3 < len(word):
  count3 += 1
  # step 2: print a line of stars above the word
  count2 = 0
  while count2 < count3:  # step 4: print a triangle
    print "*",
    count2 = count2 + 1
  print  # starts a new line

# step 1: print the word one letter at a time
count1 = 0
while count1 < len(word):
  print word[count1],
  count1 = count1 + 1  # increment!
print  # starts a new line