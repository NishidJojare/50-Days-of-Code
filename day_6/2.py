## Zero Both ends
## Write a function called zeroed code that takes a list of numbers as an argument. The code should zero (0) the first and the last number in the list. For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0].

# creating a function
def zeroed_code(numList):
    # reassigning the 1st and last element in a list
    numList[0],numList[-1]=0,0
    # printing updated list
    print(numList)
    

MyList=[1,5,23,7,1,89,4]
# calling a function
zeroed_code(MyList) # Ans : [0, 5, 23, 7, 1, 89, 0]
    