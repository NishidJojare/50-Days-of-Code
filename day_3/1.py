## Register Check 
## Write a function called register_check that checks how many students are in school. The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. Your function should return the number of students in school. Use the dictionary below. Your function should return 3. register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

b=[]
def register_check(r_check):
    for value in r_check.values():
        if value.lower()=='yes':
             b.append(value)
    print('No. of students present : ',len(b))
    
    
register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes','Pooja':'yes'}

register_check(register)
