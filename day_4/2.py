## Index of the Longest Word
## Write a function called word_index that takes one argument, a list of strings and returns the index of the longest word in the list. If there is no longest word (if all the strings are of the same length), the function should return zero (0). For example, the list below should return 2. words1 = ["Hate", "remorse", "vengeance"] And this list below, should return zero (0) words2 = ["Love", "Hate"]

def word_index(MyList):
    # sorting list in ascending order according to their length
    MyList.sort(key=len)
    # check if first and last items are of same length
    if len(MyList[0])==len(MyList[-1]):
        print('0','..All items are of same length')
    else:
        # find the item with max length in a list
        a=max(MyList,key=len)
        # find the index value of longest item
        b=MyList.index(a)
        print(f'Longest list item is : {a}')
        print(f'Index value of {a} is : {b}')
    
    
words1 = ["Hate", "remorse", "vengeance",'nishid']
words2 = ['nishid','nishid', 'nishid','nishid']
word_index(words1)
print('')
word_index(words2)
