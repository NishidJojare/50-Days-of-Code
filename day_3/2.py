## Lowercase Names

## names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]

## You are given a list of names above. This list is made up of names of lowercase and uppercase letters. Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return: ('kerry', 'dickson', 'carol', 'adam')

names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
b=[]
for i in names:
    if i==i.lower():
        b.append(i)
    b.sort(reverse=True)
print(tuple(b)) # ans : ('kerry', 'dickson', 'carol', 'adam')
        