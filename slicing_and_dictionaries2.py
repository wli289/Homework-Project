def unique_letters(word):
    """ boolean: True if all letters unique,
        False otherwise """
    for index in range(len(word)):
        if word[index] in word[index+1:]:
            return False
    return True # need to check EVERY letter first

def letter_count(word):
    """ create a dictionary that contains letter counts """
    counts = {'a':0}
    for letter in word:
        if letter in counts: # is letter a KEY
            # overwrite letter's value
            counts[letter] = counts[letter] + 1
        else:
            # insert letter into dictionary
            counts[letter] = 1
        #print counts
    for key in counts:
        print key, ":", counts[key]

letter_count('banana')
print # prints a blank line
letter_count('evuih xds vnsufh')
