## Count the Dots
## Write a function called count_dots. This function takes a string separated by dots as a parameter and counts how many dots are in the string. For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.

def count_dots(mystr):
    c=str(mystr).count('.')
    print(f'Total Dots in a given string are : {c}')
    
string1='h.e.l.p.'
string2='he.lp.'
count_dots(string1)
'''
output : Total Dots in a given string are : 4
'''

count_dots(string2)
'''
output : Total Dots in a given string are : 2
'''