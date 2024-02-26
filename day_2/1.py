## Strings to Integers

## Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. For example ['1', '3', '5'] should be converted to [1, 3, 5] and summed to 9.

b=[]
def convert_add(StrList):
    for i in StrList:
        # converting string items into int
        num = int(i)
        # appending int item in a new list
        b.append(num)
        
MyList=['1','3','5']
# passing a list of strings in a function
convert_add(MyList)
# printing new list
print('New list : ',b,'\nsum of all items of a list : ',sum(b))

