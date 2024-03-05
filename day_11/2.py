## Swap Values
## Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element. For example, if you pass [2, 4,67, 7] as a parameter, your function should return [7, 4, 67, 2].

def swap_values(mylist):
    mylist[0],mylist[-1]=mylist[-1],mylist[0]
    print(mylist)
    
mylist=[2,4,67,7]
swap_values(mylist)

'''
output : [7, 4, 67, 2]
'''

    