# Longest Value

# Write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary. For example, the following dictionary should return – apple as the longest value. fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(d):
    b=[]
    for value in d.values():
         b.append(value)
         # finnding longest value from list b, depending on string length
         longest=max(b,key=len)
    print(longest)
         
fruits = {'fruit': 'apple', 'color': 'green','str':'Strawberry'}     
longest_value(fruits) # Ans : Strawberry
          
            



            