## Are They Equal?
## Write a function called equal_strings. The function takes two strings as arguments and compares them. If the strings are equal (if they have the same characters and have equal length), it should return True, if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

def equal_strings(s1,s2):
    if len(s1)==len(s2):
        for x in s1:
            if x in s2:
                flag=True
    else:
        flag=False
        
    print(flag)
    
s1='love'    
s2='evol'    
equal_strings(s1,s2)
'''
output : True
'''