#My name: Wuding Li
import random
def create_employee():
  '''returns a dictionary representing one new randomly generated employee.'''
  employee_new  = {}
  if random.choice([True, False]) == True: #scenario if favored is ture
    employee_new = {'favored': True, 'score': random.randint(1,100)}
  else: #scenario if favored is false
    employee_new = {'favored': False, 'score': random.randint(0,99)}
  return employee_new
  
def create_company(sizes):
  '''takes in a list of the number of employees at each level and returns a list of those levels, each of which is a list of randomly generated employee dictionaries.'''
  employee = {} #create an empty dictionary
  for i, size in enumerate(sizes): #enumerate the level of the list
    employee[i]=[]
    for j in xrange(size): #building dictionary in the list of list
      d = create_employee()
      employee[i].append(d)
  return employee
  
def get_pct_favored(company, level):
  '''takes in a company list and a level to examine, and returns the percent of "favored" employees at that level.'''
  level_company = company[level] # the list of level in company
  count = 0 #set the count
  length = len(level_company) #total number of companies
  for employee in level_company:
    if employee['favored']:
      count += 1
  return count*1.0 / length

def turnover(company, sizes, pct):
  pass

def main(num_simulations, sizes, pct):
  print 'After', num_simulations, 'trails, here are the average distributions of employees:'
  favored_list = [[]for i in range(len(sizes))] #generate a list of lists, inner stores favored percent, outer stores each level
  n = 0 #initiate the running 
  while n < num_simulations:    #run as many times as num of num_simulations
    index = 0
    company = create_company(sizes) #create new company for each time of running
    for level in company:
      favored_list[index].append(get_pct_favored(company, index))
      index += 1
    n += 1
  
  print '        ','favored', 'non-favored'
  level_index = 0
  while level_index < len(company):
    #use characteristic that the level index has to smaller than the number of company
    a = sum(favored_list[level_index])/num_simulations
    print 'Level', level_index, '|', int(a * 100) , '%  |', 100-int(a * 100) , '%'
    level_index += 1
  
  return None
    
    
  
  
  
  
  
  