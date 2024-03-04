## Odd and Even
# Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and the smallest odd number in the list. For example, if you pass [1,2,4,6] as an argument the function should return 6-1= 5.

def odd_even(numList):
    even=[]
    odd=[]
    for n in numList:
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
            
    difference=max(even)-min(odd)
    print(f"Smallest odd number : {min(odd)}\nLargest even number : {max(even)}\nDifference between {max(even)} and {min(odd)} is : {difference}")
    
    
MyList=[24,10,3,4,6,9,2,5,8,7]
odd_even(MyList)


'''
output : 

Smallest odd number : 3
Largest even number : 24
Difference between 24 and 3 is : 21

'''