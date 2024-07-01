def swap_case(s):
    """
    Convert upper case letters to lower case and lower case letters to upper case.
    
    Args:
    s (str): The input string.
    
    Example:
    >>> swap_case('abA')
    ABA
    """
    result = s.swapcase()
    print(result)

def split_string(s):
    """
    Split a string by spaces.
    
    Args:
    s (str): The input string.
    
    Example:
    >>> split_string('split string')
    ['split', 'string']
    """
    result = s.split(' ')
    print(result)

def mutate_string(string, position, character):
    """
    Modify a string by changing the character at a specified position.
    
    Args:
    string (str): The input string.
    position (int): The position to modify.
    character (str): The character to insert.
    
    Example:
    >>> mutate_string('Appen String', 5, 'd')
    Append String
    """
    result = string[:position] + character + string[position+1:]
    print(result)

if __name__ == "__main__":
    print("Swap Case Example:")
    swap_case('abA')  # Output: ABA
    
    print("\nSplit String Example:")
    split_string('split string')  # Output: ['split', 'string']
    
    print("\nMutate String Example:")
    mutate_string('Appen String', 5, 'd')  # Output: Append String
