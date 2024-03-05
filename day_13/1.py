## Pay Your Tax
## Write a function called your_vat. The function takes no parameter. The function asks the user to input the price of an item and VAT (vat should be a percentage). The function should return the price of the item plus VAT. If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253. Make sure that your code can handle ValueError. Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop).

def your_vat():
    while True:
        try:
            price=float(input('Enter the price of an item : '))
            vat=float(input('Enter VAT : '))
            if price>0 and vat>0:
                vat_percent=(price*vat)/100
                result=price+vat_percent
                print(f'Inclusive price : {result}')
                break
        except ValueError as v:
            print(f'{v}')
            
            
your_vat()

'''
output : 

                    Enter the price of an item : 220
                    Enter VAT : 15
                    Inclusive price : 253.0
'''
            
            
    