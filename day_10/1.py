## Write a function called hide_password that takes no parameters. The function takes an input (a password) from a user and returns a hidden password. For example, if the user enters ‘hello’ as a password the function should return ‘****’ as a password and tell the user that the password is 4 characters  long. 

# using for loop 

# def hide_password():
#     user_pwd=input('Enter your password : ')
#     for ch in range(len(user_pwd)):
#         new=user_pwd.replace(user_pwd[ch],"*")
#         user_pwd=new
#     return user_pwd 

# print(hide_password())


# without using for loop
def hide_password():
    starlist=["*"]
    user_pwd=input('Enter your password : ')
    new=starlist*len(user_pwd)
    return ''.join(new)
print(hide_password())

'''  
output : 
                    Enter your password : Nishid@123
                    **********
'''