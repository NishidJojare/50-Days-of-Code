##Day 9: Biggest Odd Number
## Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension.

# def biggest_odd(num):
#     # biggest_odd=[x for x in num]
#     b=[]
#     for i in range(len(num)):
#         if int(num[i])%2==1:
#             b.append(int(num[i]))
#     print(max(b))
    
    
# mystr="57802"
# biggest_odd(mystr)


def biggest_odd(num):
   b=[int(num[x]) for x in range(len(num)) if int(num[x])%2==1]
   print(f"Max element is : ",max(b))
   
mystr="23569"
biggest_odd(mystr)


   