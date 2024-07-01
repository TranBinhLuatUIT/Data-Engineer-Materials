from functools import reduce

def map_example():
    """
    Demonstrates the use of the map function to apply a function to all items in an iterable.
    
    Example:
    >>> map_example()
    Squared numbers: [1, 4, 9, 16, 25]
    """
    numbers = [1, 2, 3, 4, 5]
    
    # Using map to apply a lambda function that squares each number
    squared_numbers = map(lambda x: x ** 2, numbers)
    
    # Converting map object to a list and printing the result
    print("Squared numbers:", list(squared_numbers))

def lambda_example():
    """
    Demonstrates the use of lambda functions to create small anonymous functions.
    
    Example:
    >>> lambda_example()
    Add 10 to 5: 15
    """
    # Defining a lambda function that adds 10 to a number
    add_ten = lambda x: x + 10
    
    # Using the lambda function and printing the result
    result = add_ten(5)
    print("Add 10 to 5:", result)

def reduce_example():
    """
    Demonstrates the use of the reduce function to apply a function cumulatively to the items of an iterable.
    
    Example:
    >>> reduce_example()
    Product of numbers: 120
    """
    numbers = [1, 2, 3, 4, 5]
    
    # Using reduce to calculate the product of all numbers in the list
    product = reduce(lambda x, y: x * y, numbers)
    
    # Printing the result
    print("Product of numbers:", product)

if __name__ == "__main__":
    map_example()
    lambda_example()
    reduce_example()
