# Return statements are used if a function should "return" or give a value

# For example:
def square(number):
    return number*number

# The outline of a basic function with a return statement
# def example(parameter):
    # code
    # code
    # etc
    # return [expression]

# Multiple return statements can be used in a function with multiple potential outputs 
# Example:
def name_animal_of_colour(colour: str):
    colour = colour.lower()
    if colour == "red":
        return "Red Macaw"
    elif colour == "yellow":
        return "Giraffe"
    elif colour == "green":
        return "Toad"

# A return statement will EXIT the function code block
# They can also return w/o a value and can be used to prematurely exit a function
def serve_alcohol(age: int):
    if age < 19:
        return
    order = input("What drink would you like?\n")
    print(f"One {order} is ready!")
# This technically returns None, a special "null" value in python

# Functions can return almost any value
# This includes variables, objects, constants, and even functions themselves (via references)
# Example:
def choose_function(n: int):
    FUNCTIONS = (square, name_animal_of_colour, serve_alcohol)
    if n < 0 and n >= 3:
        return
    return FUNCTIONS[n]
    
def main():
    print( choose_function(0)(4) )
    print( choose_function(1)("red") )
    print( choose_function(2)(20) )
    # > python3 main.py
    # 16
    # Red Macaw
    # What drink would you like?
    # > 

main()
