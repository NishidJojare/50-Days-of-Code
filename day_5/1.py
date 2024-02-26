## My Discount
## Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.


# Formula : price_after_discount = price - (price * discount / 100)

def my_discount():
    # getting price and discount values from user
    price=float(input('Enter the product price : '))
    discount=float(input('Enter the discount you have got in percentage(%) : '))
    
    # calculating price_after_discount and dicounted_price
    price_after_discount=price - (price * discount / 100)
    dicounted_price=(price*discount)/100
    
    # printing the caculated values
    print(f"Product price : {price}")
    print(f"Discount in percentage : {discount}")
    print(f"Discounted Price : {dicounted_price}")
    print(f"Payable amount after discount deduction : {price_after_discount}")
    
# calling the function to display the output
my_discount()

'''
Ans 1 : 

Enter the product price : 150
Enter the discount you have got in percentage(%) : 15
Product price : 150.0
Discount in percentage : 15.0
Discounted Price : 22.5
Payable amount after discount deduction : 127.5


Ans 2 :

Enter the product price : 1000
Enter the discount you have got in percentage(%) : 10
Product price : 1000.0
Discount in percentage : 10.0
Discounted Price : 100.0
Payable amount after discount deduction : 900.0

'''