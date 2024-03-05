# ## Pyramid of Snakes
# ## Write a function called Python_snakes that takes a number as an argument and creates the following shape, using the number’s range: (hint: Use the loops and emoji library. If you pass 7 as argument, your code should print the following:

'''
                   🐍 
                 🐍 🐍 
               🐍 🐍 🐍 
              🐍 🐍 🐍 🐍 
            🐍 🐍 🐍 🐍 🐍 
'''

def Python_snakes(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        snakes = " \U0001F40D" * i
        print(spaces + snakes)

num_rows = 5
Python_snakes(num_rows)

'''
output : 
                   🐍 
                 🐍 🐍 
               🐍 🐍 🐍 
              🐍 🐍 🐍 🐍 
            🐍 🐍 🐍 🐍 🐍 
'''