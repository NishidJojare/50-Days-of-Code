## User Name Generator
## Write a function called user_name that generates a username from the user’s email. The code should ask the user to input an email and the code should return everything before the @ sign as their user name. For example, if someone enters ben@gmail.com, the code should return ben as their user name.

def user_name():
    txt='@gmail.com'
    # get the email from user
    email=input("Enter your E-mail Id : ")
    # check if email is valid or not 
    if txt in email.lower():
        # find the index value of @ symbol
        f=email.find('@')
        # printing string before @ i.e. Username
        print(f'username : {email[0:f]}')
    else:
        print('Invalid')
        
        
# calling function to display output    
user_name()