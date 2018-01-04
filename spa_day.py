#My name(Wuding Li)
def main_function():
  schedules = [] #create an emply list
  print 'UW-Madison DPT Massage Fundraiser Scheduler'
  while(True):
    select = int(raw_input('Make a selection:\n1. Add a massage to my schedule\n2. View my current schedule\n3. Cancel a massage from my schedule\n4. Calculate fundraising total\n5. Quit\nYour selection:'))#the main menu
    if select == 1:
      user_schedule = int(raw_input('Add a (1) 15 minute, (2) 30 minute, or (3) 60 minute massage?')) #the sub menu for add a massage
      translated = translation(user_schedule)
      schedules.append(translated)
    elif select == 2:
      show_list(schedules) #show all current schedules
    elif select == 3:
      show_list(schedules) #show all current schedules
      if len(schedules) == 0: 
        print "Unable to cancel a massage, no massages scheduled."#when there is currently no massage in list, user cannot cancel any schedules
      else:
        cancel = int(raw_input("Which massage do you want to cancel?"))
        if (len(schedules) - 1 >= cancel and cancel >= 0):
          schedules.pop(cancel) #remove the selected schedules
    elif select == 4:
      print "Your current total is $", calculation(schedules) #call the calculation function
    elif select == 5:
      print "Goodbye!"
      break #end the program
    else:
      print "invalid input, choose from 1-5" #prevent crush if incorrect user input
    
def translation(selection):
  '''translate user's selection of 1-3 into mssage duration 15,30,60 min'''
  if selection == 1:
    return 15
  elif selection == 2:
    return 30
  elif selection == 3:
    return 60
  else:
    print "invalid input, please choose from 1-3" #prevent crush if invalid input appears
def show_list(schedules):
  print "Your day contains:"
  index = 0
  for element in schedules:
    print index, ":", element, "minute"
    index += 1
def calculation(schedules):
  total_schedules = 0
  for element in schedules:
    if element == 15:
      total_schedules += 20
    elif element == 30:
      total_schedules += 30
    elif element == 60:
      total_schedules += 60
  return total_schedules
  
main_function()