def get_num():
  num = raw_input("Number:")
  num = int(num)
  return num

def print_repeat(string_to_repeat):
  n = get_num()
  print n * string_to_repeat

print type(get_num())

print 5
print "5"

print_repeat('x')
print_repeat('apple')