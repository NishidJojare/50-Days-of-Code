## Extra Challenge: A Thousand Separator

## Your new company has a list of figures saved in a list. The issue is that these numbers have no separator. The numbers are saved in the following format: [1000000, 2356989, 2354672, 9878098]. You have been asked to write a code that will convert each of the numbers in the list into a string. Your code should then add a comma on each number as a thousand separator for readability. When you run your code on the above list, your output should be: [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’] Write a function called convert_numbers that will take one argument, a list of numbers above.
   
## 1st approach (lengthy)  
    
def convert_numbers(mylist):
    new_list=[]
    
    for x in mylist:
        empty_str=''
        c=0
        new_str=str(x)[::-1]
        for y in new_str:
            empty_str+=y
            c+=1
            if c==3:
                empty_str+=','
                c=0
                
    
        new_list.append(empty_str[::-1])
        
    print(new_list)

    
a=[1000000, 2356989, 2354672, 9878098]  
convert_numbers(a)  
   
'''
Output : ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
'''    
    
    
## 2nd approach    
    
def convert_numbers(numbers):
    formatted_numbers = [format(number, ',') for number in numbers]
    return formatted_numbers

# Example usage:
numbers_list = [1000000, 2356989, 2354672, 9878098]
formatted_list = convert_numbers(numbers_list)
print(formatted_list)

'''
Output : ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
'''
