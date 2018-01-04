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
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
            print counts
