def guess(target):
  user_guess = int(raw_input("Guess the number:"))
  if target == user_guess:
    print "You got it!"
  if target != user_guess:
    print "Wrong!"
  print "The number was", target
#guess(3)

def guess_2():
  usernum = int(raw_input("Guess the number:"))
  number = 5
  if number == usernum:
    print "You got it!"
  else:
    print "Wrong!"
  print "The number was", number
#guess_2()

def guess_3():
  user_typed_in = int(raw_input("Guess the number:"))
  we_chose = 5
  if we_chose == user_typed_in:
    print "You got it!"
  elif we_chose < user_typed_in:
      print "Too high!"
  print "The number was", we_chose
#guess_3()



import random
def guess_4():
  target = random.randint(1,10)
  x = int(raw_input("Guess the number:"))
  if x > target:
    print "Too high!"
    x = int(raw_input("Guess the number:"))
    if x == target:
      print "You got it!"
    else:
      print "Wrong!"
  elif x < target:
    print "Too low!"
    x = int(raw_input("Guess the number:"))
    if x == target:
      print "You got it!"
    else:
      print "Wrong!"
  else:
    print "You got it!"
  print "The number was", target
guess_4()
    











