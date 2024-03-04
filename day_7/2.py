## Dictionary of names
## You are given a list of names, and you are asked to write a code that returns all the names that start with ‘S’. Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary. Here is a list below: names = ["Joseph","Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera”, "Patel", "Sera”] Your code should return: {“Sasha”: 1, “Sera”: 2}


names = ["Joseph","Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera", "Patel", "Sera",'Nishid','Nishid','Nishid','Nishid','Nishid']
a=[]
b=[]
# iterating through list of names
for name in names:
    # check for the names which starts with S
    if name.startswith('S'):
        # appending names starts with S in list a
        a.append(name)
        # appending counts of names which starts with S in list b
        b.append(names.count(name))
    
# using dictionary comprehension for creating new dictionary from lists a and b
c={a:b for a,b in zip(a,b)}
# printing final output
print(c)


'''
output : {'Sasha': 1, 'Sera': 2}

'''
