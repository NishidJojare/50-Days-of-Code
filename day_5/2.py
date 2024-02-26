
## Tuple of Student Sex
## You work for a school and your boss wants to know how many female and male students are enrolled in the school. The school has saved the students in a list. Your task is to write a code that will count how many males and females are in the list. Here is a list below: students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female'] Your code should return a list of tuples. The list above should return: [(‘Male’,7), (‘female’,6)]

# creating a function for calculating males and females
def calculate_male_female(std):
    male_count=0
    female_count=0
    a='Male'
    b='Female'
    # iterating through student list
    for gender in std:
        if gender.lower()=='male':
            male_count+=1
        if gender.lower()=='female':
            female_count+=1
        
    
    myTuple1=(a,male_count)
    myTuple2=(b,female_count)
    myList=[myTuple1,myTuple2]
    print(myList)


# List of male & females
students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# calling function to display final output
calculate_male_female(students)

'''
Ans :  [('Male', 7), ('Female', 6)]
'''