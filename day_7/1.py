## A String Range
## Write a function called string_range that takes a single number and returns a string of its range. The string characters should be separated by dots(.) For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

# creating function named string_range()
def string_range(number):
    # returning numbers seperated by dot(.) by iterating through range of numbers
    return ".".join(str(i) for i in range(number))

# calling function for the final output
print(string_range(6))


'''
output: 0.1.2.3.4.5

'''