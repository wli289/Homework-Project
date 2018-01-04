d = {'a':0, 'b':4, 'c':12, 'd':2, 'e':1}
k = d.keys()

print k
print sorted(k) # does NOT sort in place (deep copy)
print k

for key in sorted(d.keys()):
    print key, ":", d[key]
