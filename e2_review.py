# list comprehension syntax
# the Point: building up a new list

result = []
for x in range(5):
    result.append(x**2)
print result  # [0, 1, 4, 9, 16]

result = [x**2 for x in range(5)]
print result  # [0, 1, 4, 9, 16]

# optional if statement
result = []
for x in range(5):
    if x % 2 == 0:
        result.append(x**2)
print result  # [0, 4, 16]

result = [x**2 for x in range(5) if x % 2 == 0]
print result  # [0, 4, 16]

##### DICTIONARIES

sample_dictionary = {'a':1, 'b':5, 'c':3}
for letter in sorted(sample_dictionary.keys()):
    print sample_dictionary[letter]
