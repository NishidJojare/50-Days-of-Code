## Duplicate Names
## Write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. If there are duplicates, the function should return the duplicates. If there are no duplicates, the function should return "No duplicates". For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates". fruits = ['apple', 'orange', 'banana', 'apple'] names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(MyList):
    b=set()
    for i in MyList:
        a=MyList.count(i)
        if a>1:
            b.add(i)
        
    if len(b)!=0:
        return b
    else:
        return 'No Duplicates'
    
    
    
fruits = ['apple', 'orange', 'banana', 'apple','Nishid','Nishid']
names = ['Yoda', 'Moses', 'Joshua', 'Mark','banana','banana','banana']

print(check_duplicates(fruits))

print(check_duplicates(names))

