## Your Age in Minutes
## Write a function called age_in_minutes that tells a user how old they are in minutes. Your code should ask the user to enter their year of birth, and it should return their age in minutes (by subtracting their year of birth to the current year). Here are things to look out for: 

# a. The user can only input a 4-digit year of birth. For example, 1930 is a valid year. However, entering any number longer or less than 4 digits long should render input invalid. Notify the user to input a four digits number. 

# b. If a user enters a year before 1900, your code should tell the user that input is invalid. If the user enters the year after the current year, the code should tell the user, to input a valid year. The code should run until the user inputs a valid year. 

# Your function should return the user's age in minutes. For example, if someone enters 1930, as their year of birth your function should return: You are 48,355,200 minutes old.


import datetime
def age_in_minutes():
    while True:
        year_of_birth=int(input('Enter your year of birth : '))
        current_year=datetime.date.today().year
        if len(str(year_of_birth))==4:
            if year_of_birth>=1900 and year_of_birth<=current_year:
                years=current_year-year_of_birth
                days=years*365.25
                hours=days*24
                mins=hours*60
                print(f'Age is minutes : {mins:,}')
                break
            else:
                print('Input a Valid Year')
            
        else:
            print('Invalid Input..make sure you are entering 4 digit year')
      
age_in_minutes()

'''
output : 

            Enter your year of birth : 1930
            Age is minutes : 49,440,240.0

            Enter your year of birth : 2002
            Age is minutes : 11,571,120.0
'''


